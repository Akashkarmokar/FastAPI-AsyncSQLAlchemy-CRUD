from .Timestamps import TimestampedModel
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import Relationship
from .Register import Register


class Link(TimestampedModel):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)

    # Foreign Fields
    register_id = Column(Integer, ForeignKey("registers.id", ondelete="CASCADE"), nullable=False, index=True, unique=True)

    # Relationships
    register = Relationship("Register", back_populates="links", passive_deletes=True)
    tags = Relationship("Tag", secondary="link_tags", back_populates="tags", passive_deletes=True)

