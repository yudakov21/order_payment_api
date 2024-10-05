from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

payment = Table(
    'payment',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('order_id', Integer, nullable=False),
    Column('payment_type', String, nullable=False),
    Column('status', String, nullable=False, default='pending'),
    Column('created_at', TIMESTAMP, nullable=False),
    Column('security_code', String, nullable=True),
    Column('email_address', String, nullable=True)
)