from base import BaseORM
import sqlite3

class Team(BaseORM):
    def create_tables(self):
        create_team_table = """
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """
        self.execute_query(create_team_table)

    def add_team(self, name):
        create_team_query = "INSERT OR IGNORE INTO teams (name) VALUES (?)"
        self.create(create_team_query, (name,))
        if self.cursor.rowcount > 0:
            print("Team added successfully.")
        else:
            print(f"Team '{name}' already exists or an error occurred.")


    @classmethod
    def find_team_by_name(cls, name):
        conn = sqlite3.connect(cls.db_name)
        cursor = conn.cursor()
        find_team_query = "SELECT * FROM teams WHERE name = ?"
        cursor.execute(find_team_query, (name,))
        result = cursor.fetchone()
        return result
    
    def delete_team(self, team_id):
        delete_team_query = "DELETE FROM teams WHERE id = ?"
        self.delete(delete_team_query, (team_id,))

    def get_all_teams(self):
        get_all_teams_query = "SELECT * FROM teams"
        return self.find_all(get_all_teams_query)

    def find_team_by_id(self, team_id):
        find_team_query = "SELECT * FROM teams WHERE id = ?"
        return self.find_by_id(find_team_query, (team_id,))
