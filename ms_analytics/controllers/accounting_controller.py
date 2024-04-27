import json

from ..dtos.output import CategoryVsPurchaseAndSalesDto, LossVsProfitChartDto


async def loss_vs_profit() -> LossVsProfitChartDto:
    with open("ms_analytics/data/data.json") as f:
        data = json.load(f)

    return LossVsProfitChartDto(
        loss=data["accounting"]["lossVsProfitPercentage"]["loss"],
        profit=data["accounting"]["lossVsProfitPercentage"]["profit"]
    )


async def category_vs_purchase_and_sales() -> CategoryVsPurchaseAndSalesDto:
    with open("ms_analytics/data/data.json") as f:
        data = json.load(f)
    
    return CategoryVsPurchaseAndSalesDto(
        categories=data["accounting"]["categoryVsPurchaseAndSales"]["categories"],
        purchase=data["accounting"]["categoryVsPurchaseAndSales"]["purchase"],
        sales=data["accounting"]["categoryVsPurchaseAndSales"]["sales"]
    )
    
    
