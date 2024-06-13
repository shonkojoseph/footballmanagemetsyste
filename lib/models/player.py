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
        self.commit_and_close()

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

# Create an instance to create the table
player_instance = Player()
player_instance.create_tables()
player_instance.commit_and_close()

# Populate players table
players_data = [
    ("Player 1", "Forward", 1),  # Assuming team_id 1 exists
    ("Player 2", "Midfielder", 2),  # Assuming team_id 2 exists
    ("Player 3", "Defender", 3)  # Assuming team_id 3 exists
]

for name, position, team_id in players_data:
    player_instance = Player()
    player_instance.add_player(name, position, team_id)
    player_instance.commit_and_close()

print("Players table populated")
