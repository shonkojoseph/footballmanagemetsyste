from team import Team
from player import Player

# Create tables for teams and players
team_instance = Team()
team_instance.create_tables()

player_instance = Player()
player_instance.create_tables()

# Populate teams table
teams_data = [
    "Team A",
    "Team B",
    "Team C"
]

for name in teams_data:
    team_instance = Team()
    team_instance.add_team(name)

print("Teams table populated")

# Populate players table
players_data = [
    ("Player 1", "Forward", 1),  # Assuming team_id 1 exists
    ("Player 2", "Midfielder", 2),  # Assuming team_id 2 exists
    ("Player 3", "Defender", 3)  # Assuming team_id 3 exists
]

for name, position, team_id in players_data:
    player_instance = Player()
    player_instance.add_player(name, position, team_id)

print("Players table populated")

# Fetch and display all teams
print("Teams:")
all_teams = team_instance.get_all_teams()
for team in all_teams:
    print(team)

# Fetch and display all players
print("Players:")
all_players = player_instance.get_all_players()
for player in all_players:
    print(player)
