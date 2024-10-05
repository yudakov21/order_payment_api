from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from app.database import get_async_session
from app.api.manager import get_user_manager
from app.api.models import User, user


router = APIRouter(
    prefix='/users', 
    tags=['Users']
)

@router.get('/{user_id}')
async def get_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(user).where(user.c.id == user_id)
        result = await session.execute(query)
        user_data = result.fetchone()

        if user_data:
            user_dict = dict(user_data._asdict())
            return user_dict
        else:
            return None
    except Exception:
        raise HTTPException(status_code= 500, detail={
                'status': 'error',
                'data': None,
                'details': None,
            })


cookie_transport = CookieTransport(cookie_name='bonds',cookie_max_age=3600)

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)   

current_user = fastapi_users.current_user()

