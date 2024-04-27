from ..dtos.output import CategoryVsPurchaseAndSalesDto, LossVsProfitChartDto
from ..helpers.data import get_data


async def loss_vs_profit() -> LossVsProfitChartDto:
    data = get_data()

    return LossVsProfitChartDto(
        loss=data["accounting"]["lossVsProfitPercentage"]["loss"],
        profit=data["accounting"]["lossVsProfitPercentage"]["profit"],
    )


async def category_vs_purchase_and_sales() -> CategoryVsPurchaseAndSalesDto:
    data = get_data()

    return CategoryVsPurchaseAndSalesDto(
        categories=data["accounting"]["categoryVsPurchaseAndSales"]["categories"],
        purchase=data["accounting"]["categoryVsPurchaseAndSales"]["purchase"],
        sales=data["accounting"]["categoryVsPurchaseAndSales"]["sales"],
    )
