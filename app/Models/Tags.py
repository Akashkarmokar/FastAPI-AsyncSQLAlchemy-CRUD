from .Timestamps import TimestampedModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Relationship


class Tag(TimestampedModel):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_title = Column(String(15), nullable=False)
    register_id = Column(Integer, ForeignKey('registers.id', ondelete="CASCADE"), nullable=False, index=True)

    # Relationships
    inserted_by = Relationship("Register", back_populates="tags")
    links = Relationship("Link", secondary="link_tags", back_populates="tags", passive_deletes=True)

