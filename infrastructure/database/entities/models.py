from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String)
    tg_id: Mapped[int] = mapped_column(Integer)
    dorm_id: Mapped[int] = mapped_column(Integer, ForeignKey('dorms.id'))
    dorm: Mapped['Dorm'] = relationship('Dorm')

class Dorm(Base):
    name: Mapped[str] = mapped_column(String)
