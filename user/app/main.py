from fastapi import FastAPI
from app.api.models import User
from fastapi_users import fastapi_users, FastAPIUsers
from app.api.user import auth_backend, router
from app.api.schemas import UserRead, UserCreate
from app.api.manager import get_user_manager

app = FastAPI(
    title='User'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router)