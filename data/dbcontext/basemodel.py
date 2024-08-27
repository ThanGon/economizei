from peewee import *
from dbcontext import ECONOMIZEICONTEXTDB

class BaseModel(Model):
    class Meta: 
        database = ECONOMIZEICONTEXTDB