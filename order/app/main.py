from fastapi import FastAPI
from app.api.order import router

app = FastAPI(
    title='Order'
)

app.include_router(router)

