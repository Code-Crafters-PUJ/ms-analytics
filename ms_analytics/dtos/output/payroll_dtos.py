from pydantic import BaseModel


class MonthVsSalaryDto(BaseModel):
    months: list[str]
    salaries: list[float]


class FortnightVsSalaryDto(BaseModel):
    fortnights: list[str]
    salaries: list[float]
