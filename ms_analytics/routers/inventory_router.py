from typing import Annotated

from fastapi import APIRouter, Depends

from ..config.constants.app import Role
from ..controllers import (
    category_vs_stock_percentage,
    product_vs_top_5_less_stock,
    provider_vs_stock_percentage,
)
from ..dtos.output import (
    CategoryVsStockPercentageDto,
    ProductVsTop5lessStockDto,
    ProviderVsStockPercentageDto,
)
from ..middlewares import validate_role

router = APIRouter()


@router.get("/category-vs-stock-percentage")
async def get_category_vs_stock_percentage(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> CategoryVsStockPercentageDto:
    return await category_vs_stock_percentage()


@router.get("/product-vs-top-5-less-stock")
async def get_product_vs_top_5_less_stock(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> ProductVsTop5lessStockDto:
    return await product_vs_top_5_less_stock()


@router.get("/provider-vs-stock-percentage")
async def get_provider_vs_stock_percentage(
    # _: Annotated[None, Depends(validate_role(Role.ADMIN))],
) -> ProviderVsStockPercentageDto:
    return await provider_vs_stock_percentage()
