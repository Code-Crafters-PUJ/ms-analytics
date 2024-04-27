from pydantic import BaseModel


class LossVsProfitDto(BaseModel):
    loss: float
    profit: float


class CategoryVsPurchaseAndSalesDto(BaseModel):
    categories: list[str]
    purchase: list[float]
    sales: list[float]
