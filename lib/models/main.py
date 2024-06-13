from team import Team
from player import Player


team_instance = Team()
team_instance.create_tables()

player_instance = Player()
player_instance.create_tables()


teams_data = [
    "Team A",
    "Team B",
    "Team C",
    
]

for name in teams_data:
    team_instance = Team()
    team_instance.add_team(name)

print("Teams table populated")


players_data = [
    ("player 1", "Forward", 1),  
    ("player 2", "Midfielder", 2), 
    ("player 3", "Defender", 3)  
]

for name, position, team_id in players_data:
    player_instance = Player()
    player_instance.add_player(name, position, team_id)

print("Players table populated")


print("Teams:")
all_teams = team_instance.get_all_teams()
for team in all_teams:
    print(team)


print("Players:")
all_players = player_instance.get_all_players()
for player in all_players:
    print(player)


