from .accounting_controller import category_vs_purchase_and_sales, loss_vs_profit
from .inventory_controller import (
    category_vs_stock_percentage,
    product_vs_top_5_less_stock,
    provider_vs_stock_percentage,
)
from .payroll_controller import fortnight_vs_salary, month_vs_salary
from .sales_controller import (
    branch_vs_sales,
    month_vs_income,
    top_saled_products_vs_sales,
)

__all__ = [
    "category_vs_purchase_and_sales",
    "loss_vs_profit",
    "category_vs_stock_percentage",
    "product_vs_top_5_less_stock",
    "provider_vs_stock_percentage",
    "fortnight_vs_salary",
    "month_vs_salary",
    "branch_vs_sales",
    "month_vs_income",
    "top_saled_products_vs_sales",
]
