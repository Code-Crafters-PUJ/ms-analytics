from pydantic import BaseModel

from ...config.constants.app import AccountingChartXOption


class AccountingChartInfoDto(BaseModel):
    x_label: AccountingChartXOption
    y_label: str = "total employees"
    x: list[str]  # Employees attrs
    y: list[int]  # Total Employees
