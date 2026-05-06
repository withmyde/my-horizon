"""Email service for handling subscriptions and sending summaries."""

import email
import imaplib
import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr
from typing import List

try:
    import markdown
except ImportError:
    markdown = None

from ..models import EmailConfig

logger = logging.getLogger(__name__)


class EmailManager:
    """Manages email subscriptions and sending summaries."""

    def __init__(self, config: EmailConfig, console=None):
        self.config = config
        self.pwd = os.getenv(self.config.password_env)
        if console is None:
            try:
                from rich.console import Console
                self.console = Console()
            except ImportError:
                class DummyConsole:
                    def print(self, *args, **kwargs):
                        print(*args, **kwargs)
                self.console = DummyConsole()
        else:
            self.console = console

        if not self.pwd and self.config.enabled:
            logger.warning(
                f"Environment variable {self.config.password_env} not set. Email features may fail."
            )
            self.console.print(f"[yellow]Warning: Environment variable {self.config.password_env} not set. Email features may fail.[/yellow]")

    def check_subscriptions(self, storage_manager):
        """Checks inbox for subscription requests and updates subscriber list.

        Processes UNSEEN emails with SUBSCRIBE/UNSUBSCRIBE subject,
        sends confirmation emails, and marks processed emails as read.
        """
        if not self.config.enabled:
            return

        try:
            mail = imaplib.IMAP4_SSL(self.config.imap_server, self.config.imap_port)
            mail.login(self.config.email_address, self.pwd)
            mail.select("INBOX")

            keyword = self.config.subscribe_keyword
            unsub_keyword = self.config.unsubscribe_keyword

            # Process all UNSEEN emails
            status, messages = mail.search(None, "UNSEEN")

            if status == "OK" and messages[0]:
                email_ids = messages[0].split()
                subscribers = storage_manager.load_subscribers()
                processed_ids = []

                for e_id in email_ids:
                    try:
                        _, msg_data = mail.fetch(e_id, "(RFC822)")
                        for response_part in msg_data:
                            if isinstance(response_part, tuple):
                                msg = email.message_from_bytes(response_part[1])

                                subject = str(msg.get("Subject") or "").strip()
                                sender = msg.get("From")

                                if not sender:
                                    continue

                                _, email_addr = parseaddr(sender)
                                if not email_addr or "@" not in email_addr:
                                    continue

                                # Skip noreply addresses
                                if "noreply" in email_addr.lower() or "no-reply" in email_addr.lower():
                                    processed_ids.append(e_id)
                                    continue

                                # Handle SUBSCRIBE
                                if subject.upper() == keyword.upper():
                                    if email_addr not in subscribers:
                                        storage_manager.add_subscriber(email_addr)
                                        subscribers = storage_manager.load_subscribers()
                                        self._send_confirmation(
                                            email_addr,
                                            "SUBSCRIBE CONFIRMED",
                                            f"订阅成功！\n\n您已成功订阅 Horizon 每日简报。\n\n退订方式：发送标题为 UNSUBSCRIBE 的邮件至 {self.config.email_address}",
                                        )
                                        logger.info(f"Added subscriber: {email_addr}")
                                        self.console.print(f"   ✓ 新订阅: {email_addr}")
                                    else:
                                        self._send_confirmation(
                                            email_addr,
                                            "ALREADY SUBSCRIBED",
                                            f"您已在订阅列表中，无需重复订阅。\n\n退订方式：发送标题为 UNSUBSCRIBE 的邮件至 {self.config.email_address}",
                                        )
                                        logger.info(f"Already subscribed: {email_addr}")
                                    processed_ids.append(e_id)

                                # Handle UNSUBSCRIBE
                                elif subject.upper() == unsub_keyword.upper():
                                    if email_addr in subscribers:
                                        storage_manager.remove_subscriber(email_addr)
                                        subscribers = storage_manager.load_subscribers()
                                        self._send_confirmation(
                                            email_addr,
                                            "UNSUBSCRIBE CONFIRMED",
                                            f"退订成功！\n\n您已成功退订 Horizon 每日简报。\n\n重新订阅：发送标题为 SUBSCRIBE 的邮件至 {self.config.email_address}",
                                        )
                                        logger.info(f"Removed subscriber: {email_addr}")
                                        self.console.print(f"   ✓ 退订: {email_addr}")
                                    else:
                                        self._send_confirmation(
                                            email_addr,
                                            "NOT SUBSCRIBED",
                                            f"您不在订阅列表中，无需退订。\n\n订阅方式：发送标题为 SUBSCRIBE 的邮件至 {self.config.email_address}",
                                        )
                                        logger.info(f"Not subscribed: {email_addr}")
                                    processed_ids.append(e_id)

                    except Exception as e:
                        logger.warning(f"Error processing email {e_id}: {e}")

                # Mark processed emails as seen/read
                for e_id in processed_ids:
                    try:
                        mail.store(e_id, "+FLAGS", "\\Seen")
                    except Exception as e:
                        logger.warning(f"Error marking email {e_id} as read: {e}")

            mail.close()
            mail.logout()
            self.console.print("   订阅扫描完成\n")

        except Exception as e:
            logger.error(f"Error checking subscriptions: {e}")
            self.console.print(f"[yellow]⚠️  订阅扫描出错: {e}[/yellow]")

    def send_daily_summary(
        self, summary_md: str, subject: str, subscribers: List[str]
    ):
        """Sends the daily summary to all subscribers."""
        if not self.config.enabled or not subscribers:
            return

        html_content = (
            markdown.markdown(summary_md)
            if markdown
            else f"<pre>{summary_md}</pre>"
        )

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
                h1, h2, h3 {{ color: #2c3e50; }}
                code {{ background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
                pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
                blockquote {{ border-left: 4px solid #ddd; padding-left: 15px; color: #777; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #888; text-align: center; border-top: 1px solid #eee; padding-top: 20px; }}
            </style>
        </head>
        <body>
            {html_content}
            <div class="footer">
                <p>Sent by {self.config.sender_name}</p>
                <p>To unsubscribe, please reply with "{self.config.unsubscribe_keyword}"</p>
            </div>
        </body>
        </html>
        """

        try:
            with smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(self.config.email_address, self.pwd)

                for subscriber in subscribers:
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = subject
                    msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                    msg["To"] = subscriber

                    text_part = MIMEText(summary_md, "plain")
                    html_part = MIMEText(html_body, "html")

                    msg.attach(text_part)
                    msg.attach(html_part)

                    try:
                        server.send_message(msg)
                        logger.info(f"Sent summary to {subscriber}")
                    except Exception as e:
                        logger.error(f"Failed to send to {subscriber}: {e}")

        except Exception as e:
            logger.error(f"SMTP Error: {e}")

    def _send_confirmation(self, to_email: str, subject: str, body: str):
        """Send a confirmation email with UTF-8 encoding for Chinese content."""
        try:
            with smtplib.SMTP_SSL(
                self.config.smtp_server, self.config.smtp_port
            ) as server:
                server.login(self.config.email_address, self.pwd)

                msg = MIMEText(body, "plain", "utf-8")
                msg["Subject"] = subject
                msg["From"] = f"{self.config.sender_name} <{self.config.email_address}>"
                msg["To"] = to_email

                server.send_message(msg)
                logger.info(f"Sent confirmation to {to_email}: {subject}")
        except Exception as e:
            logger.error(f"Failed to send confirmation to {to_email}: {e}")
