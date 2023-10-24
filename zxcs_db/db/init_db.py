from sqlalchemy import text
from zxcs_db.config import MySQLSettings
from zxcs_db.db.session import get_session


def init_db(settings: MySQLSettings):
    return get_session(settings).execute(text('SELECT 1;'))
