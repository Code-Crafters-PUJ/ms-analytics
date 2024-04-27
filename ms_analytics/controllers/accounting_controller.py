import json

from ..dtos.output import CategoryVsPurchaseAndSalesDto, LossVsProfitChartDto


async def loss_vs_profit() -> LossVsProfitChartDto:
    with open("ms_analytics/data/data.json") as f:
        data = json.load(f)

    return LossVsProfitChartDto(
        loss=data["lossVsProfitPercentage"]["loss"],
        profit=data["lossVsProfitPercentage"]["profit"]
    )


async def category_vs_purchase_and_sales() -> CategoryVsPurchaseAndSalesDto:
    with open("ms_analytics/data/data.json") as f:
        data = json.load(f)
    
    return CategoryVsPurchaseAndSalesDto(
        categories=data["categoryVsPurchaseAndSales"]["categories"],
        purchase=data["categoryVsPurchaseAndSales"]["purchase"],
        sales=data["categoryVsPurchaseAndSales"]["sales"]
    )
    
    
