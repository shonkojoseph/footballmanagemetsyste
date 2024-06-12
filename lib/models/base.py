from utils.db import connect_db

class BaseModel:
    @classmethod
    def execute(cls, query, params=None):
        conn = connect_db()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        conn.close()
        return cursor
