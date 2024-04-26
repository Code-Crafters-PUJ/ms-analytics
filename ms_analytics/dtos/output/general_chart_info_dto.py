from pydantic import BaseModel

from ...config.constants.app import GeneralChartXOption, GeneralChartYOption


class GeneralChartInfoDto(BaseModel):
    x_label: GeneralChartXOption
    y_label: GeneralChartYOption
    x: list[int | float]  # total sales or income
    y: list[int | str]  # product name or time period
