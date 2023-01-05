from fastapi_users.authentication import (
    CookieTransport,
    JWTStrategy,
)

from config import config

cookie_transport = CookieTransport(cookie_name="matcha", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=config.jwt.key, lifetime_seconds=3600)
