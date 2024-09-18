from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy import DECIMAL
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()

@mapper_registry.mapped
class User():
    __tablename__ = 'usuarios'

    id = mapped_column(Integer, primary_key=True)
    nome: Mapped[str]
    password: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    balance: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), default=0.0)
    goals = relationship('Goals', back_populates='user')

@mapper_registry.mapped
class Goals():
    __tablename__ = 'objetivos'

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    saved: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), default=0)
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))
    user = relationship('User', back_populates='goals')

@mapper_registry.mapped
class Transactions():
    __tablename__ = 'transacoes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))
    user = relationship('User', back_populates='transactions')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    # net: Mapped[str] = mapped_column(String(1))
