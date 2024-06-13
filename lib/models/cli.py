import argparse
from team import Team
from player import Player

class FootballCLI:
    def __init__(self):
        self.team_instance = Team()
        self.player_instance = Player()

    def add_team(self, name):
        self.team_instance.add_team(name)

    def add_player(self, name, position, team_id):
        self.player_instance.add_player(name, position, team_id)

    def list_teams(self):
        teams = self.team_instance.get_all_teams()
        for team in teams:
            print(team)

    def list_players(self):
        players = self.player_instance.get_all_players()
        for player in players:
            print(player)

    def run_cli(self):
        
        while(True):
            print("""
                Welcometo Football Inc.
                Options:
                  1. Add Team
                  2: Add Player
                  3: List teams
                  4: List Players
                  5: Exit
            """)

            cmd = int(input("> "))

            if cmd == 1:
                team_name = input("Enter team name: ")
                self.add_team(team_name)
            elif cmd == 2:
                pass
            elif cmd == 3:
                self.list_teams()
            elif cmd == 4:
                self.list_players()
            elif cmd == 5:
                exit()

if __name__ == '__main__':
    cli = FootballCLI()
    cli.run_cli()
