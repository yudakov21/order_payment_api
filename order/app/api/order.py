import time 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from app.api.service import get_user
from app.database import get_async_session
from app.api.models import order
from app.api.schemas import OrderCreate

router = APIRouter(
    prefix ="/orders",
    tags = ['Order']
)

@router.get('/{order_id}')
async def get_specific_orders(order_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(order).where(order.c.order_id == order_id)
        result = await session.execute(query)
        order_data = result.fetchone()
        
        if order_data:
            order_dict = dict(order_data._asdict())
            return order_dict
        else:
            return None
    except Exception:
        raise HTTPException(status_code= 500, detail={
            'status': 'error',
            'data': None,
            'details': None,
        })
    
@router.post('/')
async def add_specific_orders(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    user = await get_user(new_order.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User not found {new_order.user_id}")
    else:
        try:
            query = insert(order).values(**new_order.model_dump())
            await session.execute(query)
            await session.commit()
            return {'status': 'success'}
        except Exception:
            raise HTTPException(status_code= 500, detail={
                'status': 'error',
                'data': None,
                'details': None,
            })


