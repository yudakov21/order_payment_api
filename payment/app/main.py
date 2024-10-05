from fastapi import FastAPI
from app.api.payment import router

app = FastAPI(
    title='Payment'
)

app.include_router(router)