from player import Player
from match import Match

Player.drop_table()
Player.create_table()

player1 = Player.create(
    name="John Doe",
    position="Forward",
    age=25,
    nationality="England"
)

player2 = Player.create(
    name="Alice Smith",
    position="Midfielder",
    age=28,
    nationality="Spain"
)

print(Player.find_by_name("Alice Smith"))
print(Player.get_all())

Match.drop_table()
Match.create_table()

match1 = Match.create(
    date="2024-06-11",
    opponent="Manchester United",
    venue="Old Trafford"
)

match2 = Match.create(
    date="2024-06-10",
    opponent="Chelsea",
    venue="Stamford Bridge"
)

Match.find_by_date("2024-06-11")
print(Match.get_all())


