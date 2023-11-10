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
        excluded_paths = [path + '/' if path[-1] != '/' and path[-1] != "*"
                          else path for path in excluded_paths]
        special_paths = [path for path in excluded_paths if '*' in path]
        if len(special_paths) > 0:
            for s_path in special_paths:
                if s_path[:-1] in path:
                    return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the value of the header request Authorization"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None
