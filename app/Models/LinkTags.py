from .Timestamps import TimestampedModel
from sqlalchemy import Column, Integer, ForeignKey


class LinkTag(TimestampedModel):
    __tablename__ = 'link_tags'

    link_id = Column(Integer, ForeignKey('links.id', ondelete='CASCADE'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True)
