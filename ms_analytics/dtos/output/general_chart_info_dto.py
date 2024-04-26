from pydantic import BaseModel

from ...config.constants.app import GeneralChartXOptions, GeneralChartYOptions


class GeneralChartInfoDto(BaseModel):
    x_label: GeneralChartXOptions
    y_label: GeneralChartYOptions
    x: list[int | float]  # total sales or income
    y: list[int | str]  # product name or time period
