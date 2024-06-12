# team.py
from base import BaseORM

class Team(BaseORM):
    def create_tables(self):
        create_team_table = """
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """
        self.execute_query(create_team_table)
        self.commit_and_close()

    def add_team(self, name):
        create_team_query = "INSERT INTO teams (name) VALUES (?)"
        self.create(create_team_query, (name,))

    def delete_team(self, team_id):
        delete_team_query = "DELETE FROM teams WHERE id = ?"
        self.delete(delete_team_query, (team_id,))

    def get_all_teams(self):
        get_all_teams_query = "SELECT * FROM teams"
        return self.find_all(get_all_teams_query)

    def find_team_by_id(self, team_id):
        find_team_query = "SELECT * FROM teams WHERE id = ?"
        return self.find_by_id(find_team_query, (team_id,))



