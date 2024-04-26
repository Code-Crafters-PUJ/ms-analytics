from ..config.constants.app import GeneralChartXOptions, GeneralChartYOptions
from ..dtos.input import GeneralChartOptionsDto
from ..dtos.output import GeneralChartInfoDto


async def get_general_info(info: GeneralChartOptionsDto) -> GeneralChartInfoDto:
    return GeneralChartInfoDto(
        x_label=GeneralChartXOptions.MOST_SELLED_PRODUCTS,
        y_label=GeneralChartYOptions.INCOME,
        x=[1, 2, 3],
        y=["product1", "product2", "product3"],
    )
