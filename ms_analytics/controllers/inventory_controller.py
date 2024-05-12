from ..dtos.output import (
    CategoryVsStockPercentageDto,
    ProductVsTop5lessStockDto,
    ProviderVsStockPercentageDto,
)
from ..helpers.data import get_data


async def category_vs_stock_percentage() -> CategoryVsStockPercentageDto:
    data = get_data()

    return CategoryVsStockPercentageDto(
        categories=data["inventory"]["categoryVsStockPercentage"]["categories"],
        stock_percentage=data["inventory"]["categoryVsStockPercentage"]["stock"],
    )


async def product_vs_top_5_less_stock() -> ProductVsTop5lessStockDto:
    data = get_data()

    return ProductVsTop5lessStockDto(
        products=data["inventory"]["productVsTop5lessStock"]["products"],
        stock=data["inventory"]["productVsTop5lessStock"]["stock"],
    )


async def provider_vs_stock_percentage() -> ProviderVsStockPercentageDto:
    data = get_data()

    return ProviderVsStockPercentageDto(
        providers=data["inventory"]["providerVsStockPercentage"]["providers"],
        stock_percentage=data["inventory"]["providerVsStockPercentage"]["stock"],
    )    
