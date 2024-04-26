from pydantic import BaseModel

from ...config.constants.app import GeneralChartXOptions, GeneralChartYOptions


class GeneralChartOptionsDto(BaseModel):
    x_type: GeneralChartXOptions
    y_type: GeneralChartYOptions
