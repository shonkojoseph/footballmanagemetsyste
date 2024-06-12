from models.base import BaseModel

class Team(BaseModel):
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        query = 'INSERT INTO teams (name) VALUES (?)'
        cls.execute(query, (name,))

    @classmethod
    def delete(cls, team_id):
        query = 'DELETE FROM teams WHERE id = ?'
        cls.execute(query, (team_id,))

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM teams'
        cursor = cls.execute(query)
        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, team_id):
        query = 'SELECT * FROM teams WHERE id = ?'
        cursor = cls.execute(query, (team_id,))
        return cursor.fetchone()
