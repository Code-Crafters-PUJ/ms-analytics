from typing import Annotated

from fastapi import APIRouter, Depends

from ..config.constants.app import Role
from ..controllers import fortnight_vs_salary, month_vs_salary
from ..dtos.output import FortnightVsSalaryDto, MonthVsSalaryDto
from ..middlewares import validate_role

router = APIRouter()

@router.get("/month-vs-salary")
async def month_vs_salary_route(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))]
) -> MonthVsSalaryDto:
    return await month_vs_salary()


@router.get("/fortnight-vs-salary")
async def fortnight_vs_salary_route(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))]
) -> FortnightVsSalaryDto:
    return await fortnight_vs_salary()
    