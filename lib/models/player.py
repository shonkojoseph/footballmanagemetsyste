from base import BaseORM
import sqlite3

class Player(BaseORM):
    def create_tables(self):
        create_player_table = """
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            team_id INTEGER,
            FOREIGN KEY(team_id) REFERENCES teams(id)
        )
        """
        self.execute_query(create_player_table)

    def add_player(self, name, position, team_id):
        create_player_query = "INSERT INTO players (name, position, team_id) VALUES (?, ?, ?)"
        self.create(create_player_query, (name, position, team_id))

    @classmethod
    def find_player_by_name(cls, name):
        conn = sqlite3.connect(cls.db_name)
        cursor = conn.cursor()
        find_player_query = "SELECT * FROM players WHERE name = ?"
        cursor.execute(find_player_query, (name,))
        result = cursor.fetchone()
        conn.close()
        return result

    def delete_player(self, player_id):
        delete_player_query = "DELETE FROM players WHERE id = ?"
        self.delete(delete_player_query, (player_id,))

    def get_all_players(self):
        get_all_players_query = "SELECT * FROM players"
        return self.find_all(get_all_players_query)

    def find_player_by_id(self, player_id):
        find_player_query = "SELECT * FROM players WHERE id = ?"
        return self.find_by_id(find_player_query, (player_id,))

    def get_players_by_team(self, team_id):
        get_players_by_team_query = "SELECT * FROM players WHERE team_id = ?"
        return self.find_all(get_players_by_team_query)
