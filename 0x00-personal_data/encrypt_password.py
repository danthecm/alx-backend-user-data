#!/usr/bin/env python3
"""Module of password encryption"""
import bcrypt


def hash_password(password: str) -> bytes:
    """has passwords"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
