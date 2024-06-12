from models.player import Player
from models.match import Match

def exit_program():
    print("Exiting Football Manager. Goodbye!")
    exit()

def create_player():
    name = input("Enter player's name: ")
    position = input("Enter player's position: ")
    age = int(input("Enter player's age: "))
    nationality = input("Enter player's nationality: ")
    try:
        player = Player.create(name, position, age, nationality)
        print(f'{player} added to the team successfully')
    except Exception as exc:
        print("Error creating player: ", exc)

def delete_player():
    player_id = input("Enter the player's ID: ")
    try:
        if player := Player.find_by_id(player_id):
            player.delete()
            print(f'Player {player_id} has been removed from the team')
        else:
             print(f'Player {player_id} not found')
    except Exception as e:
        print(f"Error deleting player: {e}")

def display_players():
    players = Player.get_all()
    for player in players:
        print(player)

def find_player_by_name():
    name = input("Enter the player's name: ")
    player = Player.find_by_name(name)
    print(player) if player else print(
        f'Player {name} not found')


def schedule_match():
    date = input("Enter match date (YYYY-MM-DD): ")
    opponent = input("Enter opponent team's name: ")
    venue = input("Enter match venue: ")
    try:
        match = Match.create(date, opponent, venue)
        print(f'Match against {opponent} scheduled on {date} at {venue}')
    except Exception as exc:
        print("Error scheduling match: ", exc)

def cancel_match():
    match_date = input("Enter the match date to cancel (YYYY-MM-DD): ")
    try:
        if match := Match.find_by_date(match_date):
            match.cancel()
            print(f'Match on {match_date} has been canceled')
        else:
             print(f'Match on {match_date} not found')
    except Exception as e:
        print(f"Error canceling match: {e}")

def display_matches():
    matches = Match.get_all()
    for match in matches:
        print(match)

def find_match_by_date():
    date = input("Enter the match date: ")
    match = Match.find_by_date(date)
    print(match) if match else print(
        f'Match on {date} not found')

