"""Exceptions for the CISO Assistant API client."""


class CISOAssistantError(Exception):
    """Base exception for CISO Assistant API client."""


class CISOAssistantAPIError(CISOAssistantError):
    """Exception raised when the API returns an error."""


class CISOAssistantValidationError(CISOAssistantError):
    """Exception raised when response validation fails."""
