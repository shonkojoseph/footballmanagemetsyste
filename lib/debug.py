# debug.py
from player import Player
from team import Team

def main():
    while True:
        print("\nFootball Management System")
        print("1. Add Team")
        print("2. Delete Team")
        print("3. View All Teams")
        print("4. Find Team by ID")
        print("5. Add Player")
        print("6. Delete Player")
        print("7. View All Players")
        print("8. Find Player by ID")
        print("9. View Players by Team")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter team name: ")
            team = Team()
            team.add_team(name)
            print("Team added successfully.")
        
        elif choice == '2':
            team_id = int(input("Enter team ID to delete: "))
            team = Team()
            team.delete_team(team_id)
            print("Team deleted successfully.")
        
        elif choice == '3':
            team = Team()
            teams = team.get_all_teams()
            print("Teams:")
            for t in teams:
                print(t)
        
        elif choice == '4':
            team_id = int(input("Enter team ID to find: "))
            team = Team()
            t = team.find_team_by_id(team_id)
            if t:
                print("Team:", t)
            else:
                print("Team not found.")
        
        elif choice == '5':
            name = input("Enter player name: ")
            position = input("Enter player position: ")
            team_id = int(input("Enter team ID: "))
            player = Player()
            player.add_player(name, position, team_id)
            print("Player added successfully.")
        
        elif choice == '6':
            player_id = int(input("Enter player ID to delete: "))
            player = Player()
            player.delete_player(player_id)
            print("Player deleted successfully.")
        
        elif choice == '7':
            player = Player()
            players = player.get_all_players()
            print("Players:")
            for p in players:
                print(p)
        
        elif choice == '8':
            player_id = int(input("Enter player ID to find: "))
            player = Player()
            p = player.find_player_by_id(player_id)
            if p:
                print("Player:", p)
            else:
                print("Player not found.")
        
        elif choice == '9':
            team_id = int(input("Enter team ID to view players: "))
            player = Player()
            players = player.get_players_by_team(team_id)
            print("Players in team:")
            for p in players:
                print(p)
        
        elif choice == '10':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
