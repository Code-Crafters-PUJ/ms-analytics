import json

from ..config.constants.app import GeneralChartXOption, GeneralChartYOption
from ..dtos.output import GeneralChartInfoDto


async def get_general_info(
    x_type: GeneralChartXOption, y_type: GeneralChartYOption
) -> GeneralChartInfoDto:
    with open("ms_analytics/data/data.json") as f:
        data = json.load(f)

    return GeneralChartInfoDto(
        x_label=x_type,
        y_label=y_type,
        x=data["general"]["x"][x_type.value],
        y=data["general"]["y"][y_type.value],
    )
