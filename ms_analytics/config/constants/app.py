from enum import Enum


class GeneralChartXOption(Enum):
    MOST_SELLED_PRODUCTS = "most_selled_products"
    TIME_PERIODS = "time_periods"


class GeneralChartYOption(Enum):
    TOTAL_SALES = "total_sales"
    INCOME = "income"


class AccountingChartXOption(Enum):
    CONTRACT_TYPE = "contract_type"
    STATUS = "status"


class AccountingContractType(Enum):
    DEFINED = "defined"
    UNDEFINED = "undefined"
    PROVISION_OF_SERVICES = "provision_of_services"


class AccountingStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
