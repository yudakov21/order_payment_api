from pydantic import BaseModel
from abc import ABC, abstractmethod
from datetime import datetime

class PaymentRequest(BaseModel):
    id: int
    order_id: int
    payment_type: str
    status: str
    created_at: datetime
    security_code: str = None
    email_address: str = None
    

class PaymentProcessorContext:
    def __init__(self, processor):
        self.processor = processor
    
    def process_payment(self, payment_request, order):
        self.processor.process(payment_request, order)

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, payment_request, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def process(self, payment_request, order):
        print('Processing debit payment type')
        print(f"Verifying {payment_request.security_code}")
        order['status'] = 'paid'

class CreditPaymentProcessor(PaymentProcessor):
    def process(self, payment_request, order):
        print('Processing credit payment type')
        print(f"Verifying {payment_request.security_code}")
        order['status'] = 'paid'

class PaypalPaymentProcessor(PaymentProcessor):
    def process(self, payment_request, order):
        print('Processing PayPal payment type')
        print(f"Verifying {payment_request.email_address}")
        order['status'] = 'paid'

class PaymentProcessorFactory:
    @staticmethod
    def get_processor(payment_type: str):
        if payment_type == 'debit':
            return DebitPaymentProcessor()
        elif payment_type == 'credit':
            return CreditPaymentProcessor()
        elif payment_type == 'paypal':
            return PaypalPaymentProcessor()
        return None

class PaymentFacade:
    @staticmethod
    def payment_facade(payment_type: str, payment_request: PaymentRequest, order: dict):
        processor = PaymentProcessorFactory.get_processor(payment_type)
        if not processor:
            raise ValueError(f"Unknown payment type: {payment_type}")
        context = PaymentProcessorContext(processor)
        context.process_payment(payment_request, order)

class OrderAdapter:
    @staticmethod
    def adapt(order_response):
        return order_response