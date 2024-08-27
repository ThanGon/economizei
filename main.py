from .data.dbcontext.dbcontext import ECONOMIZEICONTEXTDB
from .data.user import User

ECONOMIZEICONTEXTDB.connect()

ECONOMIZEICONTEXTDB.create_tables([User])

ECONOMIZEICONTEXTDB.close()