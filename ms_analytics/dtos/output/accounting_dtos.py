from pydantic import BaseModel


class LossVsProfitChartDto(BaseModel):
    loss: float
    profit: float


class CategoryVsPurchaseAndSalesDto(BaseModel):
    categories: list[str]
    purchase: list[float]
    sales: list[float]
