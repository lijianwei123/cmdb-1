# -*- coding:utf-8 -*-
from jose import jwt

from apps import app


JWT_ALGORITHM = app.config.get('JWT_ALGORITHM', "HS256")


def jwt_encode(content, secret="secret"):
    return jwt.encode(content, secret, algorithm=JWT_ALGORITHM)


def jwt_decode(token: str, secret="secret"):
    return jwt.decode(token, secret, algorithms=(JWT_ALGORITHM, ))
