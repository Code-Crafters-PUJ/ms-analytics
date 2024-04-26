from typing import Callable

from fastapi import Header, HTTPException

from ..config.constants.app import Role
from ..helpers.jwt import get_payload


def validate_role(*roles: Role) -> Callable[[str | None], None]:
    def validate_role(token: str | None = Header(None)) -> None:
        # if token is None:
        #     raise HTTPException(status_code=401, detail="Token is required")

        # try:
        #     payload = get_payload(token)
        # except Exception:
        #     raise HTTPException(status_code=401, detail="Invalid token")

        # if payload["Role"] not in roles:
        #     raise HTTPException(status_code=403, detail="Forbidden")
        ...

    return validate_role
