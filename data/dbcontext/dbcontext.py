from playhouse.db_url import connect
import os

ECONOMIZEICONTEXTDB = connect(os.environ.get("CONNECTIONURL"))