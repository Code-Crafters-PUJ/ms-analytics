from ..config.constants.app import GeneralChartXOption, GeneralChartYOption
from ..dtos.output import GeneralChartInfoDto


async def get_general_info(
    x_type: GeneralChartXOption, y_type: GeneralChartYOption
) -> GeneralChartInfoDto:
    return GeneralChartInfoDto(
        x_label=x_type,
        y_label=y_type,
        x=[1, 2, 3],
        y=["product1", "product2", "product3"],
    )
