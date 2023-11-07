#!/usr/bin/env python3
"""Custom Authentication Module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a path"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        excluded_paths = [path + '/' if path[-1] !=
                          '/' else path for path in excluded_paths]
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the value of the header request Authorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None
