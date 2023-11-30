from .Base import Base
from sqlalchemy import Column, DateTime, func
from datetime import datetime


class TimestampedModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
