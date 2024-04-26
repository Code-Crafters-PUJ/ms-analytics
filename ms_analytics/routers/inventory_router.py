from typing import Annotated

from fastapi import APIRouter, Depends

from ms_analytics.config.constants.app import Role

from ..middlewares import validate_role

router = APIRouter()

@router.get("/info")
async def get_info_inventory(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
    x_type: None,
    y_type: None,
) -> None:
    ...