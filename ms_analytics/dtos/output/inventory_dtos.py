from pydantic import BaseModel


class CategoryVsStockPercentageDto(BaseModel):
    categories: list[str]
    stock_percentage: list[float]


class ProductVsTop5lessStockDto(BaseModel):
    products: list[str]
    stock: list[int]


class ProviderVsStockPercentageDto(BaseModel):
    providers: list[str]
    stock_percentage: list[float]
