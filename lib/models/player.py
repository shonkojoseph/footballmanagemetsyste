from models.base import BaseModel

class Player(BaseModel):
    def __init__(self, name, team_id):
        self.name = name
        self.team_id = team_id

    @classmethod
    def create(cls, name, team_id):
        query = 'INSERT INTO players (name, team_id) VALUES (?, ?)'
        cls.execute(query, (name, team_id))

    @classmethod
    def delete(cls, player_id):
        query = 'DELETE FROM players WHERE id = ?'
        cls.execute(query, (player_id,))

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM players'
        cursor = cls.execute(query)
        return cursor.fetchall()

    @classmethod
    def find_by_id(cls, player_id):
        query = 'SELECT * FROM players WHERE id = ?
