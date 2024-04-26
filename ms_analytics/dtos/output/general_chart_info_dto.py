from pydantic import BaseModel

from ...config.constants.app import GeneralChartXOption, GeneralChartYOption


class GeneralChartInfoDto(BaseModel):
    x_label: GeneralChartXOption
    y_label: GeneralChartYOption
    x: list[int | str]  # most selled products or time period
    y: list[int | float]  # total sales or income
