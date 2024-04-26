from enum import Enum


class GeneralChartXOption(Enum):
    MOST_SELLED_PRODUCTS = "most_selled_products"
    TIME_PERIODS = "time_periods"


class GeneralChartYOption(Enum):
    TOTAL_SALES = "total_sales"
    INCOME = "income"


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
