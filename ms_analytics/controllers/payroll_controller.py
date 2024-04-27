from ..dtos.output import FortnightVsSalaryDto, MonthVsSalaryDto
from ..helpers.data import get_data


async def month_vs_salary() -> MonthVsSalaryDto:
    data = get_data()

    return MonthVsSalaryDto(
        months=data["payroll"]["monthVsSalary"]["months"],
        salaries=data["payroll"]["monthVsSalary"]["salaries"],
    )


async def fortnight_vs_salary() -> FortnightVsSalaryDto:
    data = get_data()

    return FortnightVsSalaryDto(
        fortnights=data["payroll"]["fortnightVsSalary"]["fortnights"],
        salaries=data["payroll"]["fortnightVsSalary"]["salaries"],
    )