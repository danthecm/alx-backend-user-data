#!/usr/bin/env python3
"""Custom Authentication Module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Return the value of the header request Authorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None
