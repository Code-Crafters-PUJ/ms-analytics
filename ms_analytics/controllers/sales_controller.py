from ..dtos.output import BranchVsSalesDto, MonthVsIncomeDto, TopSaledProductsVsSalesDto
from ..helpers.data import get_data


async def top_saled_products_vs_sales() -> TopSaledProductsVsSalesDto:
    data = get_data()

    return TopSaledProductsVsSalesDto(
        products=data["sales"]["topSaledProductsVsSales"]["products"],
        sales=data["sales"]["topSaledProductsVsSales"]["sales"],
    )


async def month_vs_income() -> MonthVsIncomeDto:
    data = get_data()

    return MonthVsIncomeDto(
        months=data["sales"]["monthVsIncome"]["months"],
        income=data["sales"]["monthVsIncome"]["income"],
    )


async def branch_vs_sales() -> BranchVsSalesDto:
    data = get_data()

    return BranchVsSalesDto(
        branches=data["sales"]["branchVsSales"]["branches"],
        sales=data["sales"]["branchVsSales"]["sales"],
    )
