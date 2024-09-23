from datetime import datetime
from decimal import Decimal
from sqlalchemy import Enum
from typing import List

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy import DECIMAL
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

from enums.netValue import NetValue

mapper_registry = registry()

class Savings:
    pass

@mapper_registry.mapped
class User():
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True)
    nome: Mapped[str]
    password: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    balance: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), default=0.0)
    goals = relationship('Goals', back_populates='user')
    savings = relationship('Savings', back_populates='user')
    transactions = relationship('Transactions', back_populates='user')
    loans = relationship('Loans', back_populates='user')

@mapper_registry.mapped
class Goals():
    __tablename__ = 'goals'

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    # saved: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), default=0)
    goal: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), default=0)
    estimatedDate: Mapped[datetime] = mapped_column(DateTime)
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))
    user  = relationship('User', back_populates='goals')
    savings: Mapped[List[Savings]] = relationship('Savings', back_populates='goals')

@mapper_registry.mapped
class Savings():
    __tablename__ = 'savings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    saved: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    monthlySaving: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))
    user = relationship('User', back_populates='savings')
    goals: Mapped[List[Goals]] = relationship('Goals', back_populates='savings')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    interestRate: Mapped[Decimal] = mapped_column(DECIMAL(1, 2))

@mapper_registry.mapped
class Transactions():
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))
    user = relationship('User', back_populates='transactions')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    net: Mapped[NetValue] = mapped_column(Enum(NetValue))

@mapper_registry.mapped
class Loans():
    __tablename__ = 'loans'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))  
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id'))
    user = relationship('User', back_populates='loans')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    interestRate: Mapped[Decimal] = mapped_column(DECIMAL(1, 2))
    monthlyPayment: Mapped[Decimal] = mapped_column(DECIMAL(10, 2))
    startDate: Mapped[datetime] = mapped_column(DateTime)
    endDate: Mapped[datetime] = mapped_column(DateTime)