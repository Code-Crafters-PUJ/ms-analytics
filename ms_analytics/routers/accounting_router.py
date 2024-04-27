from typing import Annotated

from fastapi import APIRouter, Depends

from ..config.constants.app import Role
from ..controllers import category_vs_purchase_and_sales, loss_vs_profit
from ..dtos.output import CategoryVsPurchaseAndSalesDto, LossVsProfitDto
from ..middlewares import validate_role

router = APIRouter()


@router.get("/loss-vs-profit")
async def get_loss_vs_profit(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> LossVsProfitDto:
    return await loss_vs_profit()


@router.get("/category-vs-purchase-and-sales")
async def get_category_vs_purchase_and_sales(
    _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> CategoryVsPurchaseAndSalesDto:
    return await category_vs_purchase_and_sales()
