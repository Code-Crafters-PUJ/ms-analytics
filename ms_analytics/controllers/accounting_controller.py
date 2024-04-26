import json

from ..config.constants.app import AccountingChartXOption
from ..dtos.output import AccountingChartInfoDto


async def get_accounting_info(x_type: AccountingChartXOption) -> AccountingChartInfoDto:
    with open("ms_analytics/data/data.json") as f:
        data = json.load(f)

    return AccountingChartInfoDto(
        x_label=x_type,
        x=data["accounting"]["x"][x_type.value],
        y=data["accounting"]["y"],
    )
