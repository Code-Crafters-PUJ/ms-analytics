from fastapi import FastAPI

from .routers import general_router

app = FastAPI()


app.include_router(router=general_router, prefix="/general", tags=["general"])
