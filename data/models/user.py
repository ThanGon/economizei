from datetime import datetime

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship


mapper_registry = registry()

@mapper_registry.mapped
class User:
    __tablename__ = 'usuarios'

    id = mapped_column(Integer, primary_key=True)
    nome: Mapped[str]
    password: Mapped[str] = mapped_column(String(64))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())