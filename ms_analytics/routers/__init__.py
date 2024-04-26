from .accounting_router import router as accounting_router
from .general_router import router as general_router
from .inventory_router import router as inventory_router
from .payroll_router import router as payroll_router
from .sales_router import router as sales_router

__all__ = [
    "general_router",
    "accounting_router",
    "inventory_router",
    "payroll_router",
    "sales_router",
]
