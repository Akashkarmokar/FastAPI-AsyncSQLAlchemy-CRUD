from .Base import Base
from sqlalchemy import Column, DateTime
from datetime import datetime


class TimestampedModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow(), nullable=False)
