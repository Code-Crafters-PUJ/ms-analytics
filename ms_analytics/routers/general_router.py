from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ..config.constants.app import Role
from ..controllers import (
    category_vs_stock_percentage,
    loss_vs_profit,
    month_vs_salary,
    top_saled_products_vs_sales,
)
from ..dtos.output import (
    CategoryVsStockPercentageDto,
    LossVsProfitDto,
    MonthVsSalaryDto,
    TopSaledProductsVsSalesDto,
)
from ..middlewares.role_middleware import validate_role

router = APIRouter()


@router.get("/category-vs-stock-percentage")
async def get_category_vs_stock_percentage(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> JSONResponse:
    return JSONResponse(
        jsonable_encoder(await category_vs_stock_percentage()),
        headers={
            "Content-Disposition": 'inline; filename="out.json"',
            "encoding": "utf-8",
        },
    )


@router.get("/loss-vs-profit")
async def get_loss_vs_profit(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> LossVsProfitDto:
    return await loss_vs_profit()


@router.get("/month-vs-salary")
async def get_month_vs_salary(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> MonthVsSalaryDto:
    return await month_vs_salary()


@router.get("/top-saled-products-vs-sales")
async def get_top_saled_products_vs_sales(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> TopSaledProductsVsSalesDto:
    return await top_saled_products_vs_sales()
