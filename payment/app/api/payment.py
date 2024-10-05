from fastapi import APIRouter, Depends, HTTPException
from app.api.service import get_order
from app.api.schemas import PaymentRequest
from app.api.schemas import PaymentFacade 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from app.database import get_async_session
from app.api.models import payment

router = APIRouter(
    prefix='/payments', tags=['Payments']
)

@router.post("/pay/")
async def pay(payment_request: PaymentRequest, session: AsyncSession = Depends(get_async_session)):
    order = await get_order(payment_request.order_id)

    try:
        PaymentFacade.payment_facade(payment_request.payment_type, payment_request, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with ID {payment_request.order_id} not found.")
    else:
        try:
            query = insert(payment).values(**payment_request.dict())
            await session.execute(query)
            await session.commit()
            return {"message": "Payment processed",
                    "order": order}
        except Exception:
            raise HTTPException(status_code= 500, detail={
                'status': 'error',
                'data': None,
                'details': None,
            })    

@router.get('/')
async def get_specific_payments(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(payment).where(payment.c.id == id)
        result = await session.execute(query)
        pay_data = result.fetchone()
        
        if pay_data:
            pay_dict = dict(pay_data._asdict())
            return {
                'status': 'success',
                'data': pay_dict,
                'details': None,
            }
        else:
            return {
            'status': 'error',
            'data': None,
            'details': None,
            }
    except Exception:
        raise HTTPException(status_code= 500, detail={
            'status': 'error',
            'data': None,
            'details': None,
        })