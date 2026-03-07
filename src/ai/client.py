"""AI client abstraction supporting multiple providers."""

import os
from abc import ABC, abstractmethod
from typing import Any

from anthropic import AsyncAnthropic
from openai import AsyncOpenAI
from google import genai
from google.genai import types

from ..models import AIConfig, AIProvider


def _coerce_text_content(content: Any) -> str:
    """Extract plain text from provider-specific response payloads."""

    if content is None:
        return ""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = [_coerce_text_content(part) for part in content]
        return "\n".join(part for part in parts if part).strip()
    if isinstance(content, dict):
        for key in ("text", "content", "output_text"):
            if key in content:
                return _coerce_text_content(content[key])
        return ""

    for attr in ("text", "content", "output_text"):
        if hasattr(content, attr):
            return _coerce_text_content(getattr(content, attr))

    return str(content).strip()


def _extract_openai_message_text(response: Any) -> str:
    """Handle OpenAI-compatible responses that may return structured content."""

    choices = getattr(response, "choices", None) or []
    if not choices:
        text = _coerce_text_content(getattr(response, "output_text", None))
        if text:
            return text
        raise ValueError("OpenAI response did not include any choices.")

    message = getattr(choices[0], "message", None)
    if message is None:
        raise ValueError("OpenAI response is missing the first choice message.")

    text = _coerce_text_content(getattr(message, "content", None))
    if text:
        return text

    refusal = _coerce_text_content(getattr(message, "refusal", None))
    if refusal:
        raise ValueError(f"OpenAI response refused the request: {refusal}")

    if getattr(message, "tool_calls", None):
        raise ValueError("OpenAI response returned tool calls instead of text content.")

    text = _coerce_text_content(getattr(response, "output_text", None))
    if text:
        return text

    raise ValueError("OpenAI response did not include text content.")


class AIClient(ABC):
    """Abstract base class for AI clients."""

    @abstractmethod
    async def complete(
        self,
        system: str,
        user: str,
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> str:
        """Generate completion from AI model.

        Args:
            system: System prompt
            user: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate

        Returns:
            str: Generated completion text
        """
        pass


class AnthropicClient(AIClient):
    """Client for Anthropic Claude models."""

    def __init__(self, config: AIConfig):
        """Initialize Anthropic client.

        Args:
            config: AI configuration
        """
        api_key = os.getenv(config.api_key_env)
        if not api_key:
            raise ValueError(f"Missing API key: {config.api_key_env}")

        kwargs = {"api_key": api_key}
        if config.base_url:
            kwargs["base_url"] = config.base_url

        self.client = AsyncAnthropic(**kwargs)
        self.model = config.model
        self.max_tokens = config.max_tokens

    async def complete(
        self,
        system: str,
        user: str,
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> str:
        """Generate completion using Claude.

        Args:
            system: System prompt
            user: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate

        Returns:
            str: Generated text
        """
        message = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system,
            messages=[{"role": "user", "content": user}]
        )

        text = _coerce_text_content(message.content)
        if not text:
            raise ValueError("Anthropic response did not include text content.")
        return text


class OpenAIClient(AIClient):
    """Client for OpenAI models."""

    def __init__(self, config: AIConfig):
        """Initialize OpenAI client.

        Args:
            config: AI configuration
        """
        api_key = os.getenv(config.api_key_env)
        if not api_key:
            raise ValueError(f"Missing API key: {config.api_key_env}")

        kwargs = {"api_key": api_key}
        if config.base_url:
            kwargs["base_url"] = config.base_url

        self.client = AsyncOpenAI(**kwargs)
        self.model = config.model
        self.max_tokens = config.max_tokens

    async def complete(
        self,
        system: str,
        user: str,
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> str:
        """Generate completion using OpenAI.

        Args:
            system: System prompt
            user: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate

        Returns:
            str: Generated text
        """
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return _extract_openai_message_text(response)


class GeminiClient(AIClient):
    """Client for Google Gemini models."""

    def __init__(self, config: AIConfig):
        """Initialize Gemini client.

        Args:
            config: AI configuration
        """
        api_key = os.getenv(config.api_key_env)
        if not api_key:
            raise ValueError(f"Missing API key: {config.api_key_env}")

        self.client = genai.Client(api_key=api_key)
        self.model = config.model
        self.temperature = config.temperature
        self.max_tokens = config.max_tokens

    async def complete(
        self,
        system: str,
        user: str,
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> str:
        """Generate completion using Gemini.

        Args:
            system: System prompt
            user: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate

        Returns:
            str: Generated text
        """
        response = await self.client.aio.models.generate_content(
            model=self.model,
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )

        text = _coerce_text_content(getattr(response, "text", None))
        if text:
            return text

        text = _coerce_text_content(getattr(response, "candidates", None))
        if text:
            return text

        raise ValueError("Gemini response did not include text content.")


def create_ai_client(config: AIConfig) -> AIClient:
    """Factory function to create appropriate AI client.

    Args:
        config: AI configuration

    Returns:
        AIClient: Initialized AI client

    Raises:
        ValueError: If provider is not supported
    """
    if config.provider == AIProvider.ANTHROPIC:
        return AnthropicClient(config)
    elif config.provider == AIProvider.OPENAI:
        return OpenAIClient(config)
    elif config.provider == AIProvider.GEMINI:
        return GeminiClient(config)
    elif config.provider == AIProvider.DOUBAO:
        return OpenAIClient(config)
    else:
        raise ValueError(f"Unsupported AI provider: {config.provider}")
