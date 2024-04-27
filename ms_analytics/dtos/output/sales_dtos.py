from pydantic import BaseModel


class TopSaledProductsVsSalesDto(BaseModel):
    products: list[str]
    sales: list[float]


class MonthVsIncomeDto(BaseModel):
    months: list[str]
    income: list[float]


class BranchVsSalesDto(BaseModel):
    branches: list[str]
    sales: list[float]
