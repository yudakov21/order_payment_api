from sqlalchemy import Column, Table, Integer, String, TIMESTAMP, Float, MetaData, ForeignKey, Boolean
from datetime import datetime

metadata = MetaData()

order = Table(
    'order',
    metadata,
    Column('order_id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('name', String, nullable=False),
    Column('quantity', Integer, nullable=False),
    Column('price', Float, nullable=False),
    Column('created_at', TIMESTAMP, nullable=False)
)