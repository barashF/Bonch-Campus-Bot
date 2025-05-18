from sqlalchemy import Integer, String, ForeignKey, DateTime, Text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from datetime import datetime

from .base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    room: Mapped[int] = mapped_column(Integer, nullable=False)
    tg_id: Mapped[int] = mapped_column(BigInteger)
    dorm_id: Mapped[int] = mapped_column(Integer, ForeignKey('dorms.id', name='user_dorm_fk', onupdate="RESTRICT"))

    dorm: Mapped['Dorm'] = relationship('Dorm', lazy="subquery", back_populates="users")
    data: Mapped[dict] = mapped_column(
        MutableDict.as_mutable(JSONB), default={"privilege": "user"},
    )

class Event(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    datetime: Mapped[datetime] = mapped_column(DateTime)
    dorm_id: Mapped[int] = mapped_column(Integer, ForeignKey('dorms.id', name='event_dorm_fk', onupdate="RESTRICT"))
    
    data: Mapped[dict] = mapped_column(
        MutableDict.as_mutable(JSONB), nullable=True
    )

class Dorm(Base):
    name: Mapped[str] = mapped_column(String, unique=True)
    
    users = relationship(
        "User",
        cascade="all, delete-orphan",
        lazy="subquery",
        back_populates='dorm'
    )
    
    events = relationship(
        "Event",
        cascade="all, delete-orphan",
        lazy="subquery"
    )
    
    
