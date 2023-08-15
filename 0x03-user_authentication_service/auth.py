#!/usr/bin/env python3
""" Authentication helper class
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
       Hashes the input password with a salt using bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())
