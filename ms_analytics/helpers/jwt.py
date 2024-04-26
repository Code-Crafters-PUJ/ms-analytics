from typing import Any

from jose import jwt

from ..config.constants.environment import JWT_SECRET


def get_payload(jwt_token: str) -> dict[str, Any]:
    return jwt.decode(jwt_token, JWT_SECRET)
