#!/usr/bin/env python3
"""Module of basic authentication"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication class"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract base64 authorization header"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
