import peewee
from .dbcontext.basemodel import BaseModel

class User(BaseModel):
    username = peewee.CharField(30, unique=True)
    password = peewee.FixedCharField(72, unique=True)
    created_at = peewee.TimestampField(),
    balance = peewee.DecimalField()