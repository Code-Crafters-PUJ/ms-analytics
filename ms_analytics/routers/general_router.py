from typing import Annotated

from fastapi import APIRouter, Depends

from ..config.constants.app import GeneralChartXOption, GeneralChartYOption, Role
from ..controllers import get_general_info
from ..dtos.output import GeneralChartInfoDto
from ..middlewares import validate_role

router = APIRouter()


@router.get("/info")
async def get_info_general(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
    x_type: GeneralChartXOption,
    y_type: GeneralChartYOption,
) -> GeneralChartInfoDto:
    return await get_general_info(x_type, y_type)
