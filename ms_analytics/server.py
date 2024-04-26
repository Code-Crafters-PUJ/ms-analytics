from fastapi import FastAPI

from .routers import (
    accounting_router,
    general_router,
    inventory_router,
    payroll_router,
    sales_router,
)

app = FastAPI()

app.include_router(router=general_router, prefix="/general", tags=["general"])
app.include_router(router=accounting_router, prefix="/accounting", tags=["accounting"])
app.include_router(router=inventory_router, prefix="/inventory", tags=["inventory"])
app.include_router(router=payroll_router, prefix="/payroll", tags=["payroll"])
app.include_router(router=sales_router, prefix="/sales", tags=["sales"])
