"""Custom exceptions for the application."""

from fastapi import HTTPException


class NotFoundException(HTTPException):
    """Resource not found (404)."""

    def __init__(self, detail: str = "Resource not found"):
        super().__init__(status_code=404, detail=detail)


class ValidationException(HTTPException):
    """Validation error (422)."""

    def __init__(self, detail: str = "Validation error"):
        super().__init__(status_code=422, detail=detail)
