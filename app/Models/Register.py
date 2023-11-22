# from app.Core.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String
# from app.Models.Base import Base
from .Timestamps import TimestampedModel
from sqlalchemy.orm import Relationship


class Register(TimestampedModel):
    __tablename__ = 'registers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    # Relationships
    links = Relationship("Link", back_populates="register", passive_deletes=True)
    tags = Relationship("Tag", back_populates="inserted_by", passive_deletes=True)

