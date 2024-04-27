from pydantic import BaseModel


class CategoryVsStockPercentageDto(BaseModel):
    categories: str
    stock_percentage: float


class ProductVsTop5lessStockDto(BaseModel):
    products: str
    stock: int


class ProviderVsStockPercentageDto(BaseModel):
    providers: str
    stock_percentage: float
