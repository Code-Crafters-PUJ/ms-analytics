from fastapi import APIRouter

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

router = APIRouter()


@router.get("/category-vs-stock-percentage")
async def get_category_vs_stock_percentage() -> CategoryVsStockPercentageDto:
    return await category_vs_stock_percentage()


@router.get("/loss-vs-profit")
async def get_loss_vs_profit() -> LossVsProfitDto:
    return await loss_vs_profit()


@router.get("/month-vs-salary")
async def get_month_vs_salary() -> MonthVsSalaryDto:
    return await month_vs_salary()


@router.get("/top-saled-products-vs-sales")
async def get_top_saled_products_vs_sales() -> TopSaledProductsVsSalesDto:
    return await top_saled_products_vs_sales()
