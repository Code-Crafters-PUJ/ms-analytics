from typing import Annotated

from fastapi import APIRouter, Depends

from ms_analytics.controllers.sales_controller import (
    branch_vs_sales,
    month_vs_income,
    top_saled_products_vs_sales,
)
from ms_analytics.dtos.output.sales_dtos import (
    BranchVsSalesDto,
    MonthVsIncomeDto,
    TopSaledProductsVsSalesDto,
)

from ..config.constants.app import Role
from ..middlewares import validate_role

router = APIRouter()


@router.get("/branch-vs-sales")
async def get_branch_vs_sales(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> BranchVsSalesDto:
    return await branch_vs_sales()


@router.get("/month-vs-income")
async def get_month_vs_income(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> MonthVsIncomeDto:
    return await month_vs_income()


@router.get("/top-saled-products-vs-sales")
async def get_top_saled_products_vs_sales(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> TopSaledProductsVsSalesDto:
    return await top_saled_products_vs_sales()
