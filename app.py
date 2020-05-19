"""
Python Web TechDegree
--------------------------
Basketball Stats Tool - Project 2

"""




import constants



class Player:
    # Cleans the information of the player and assign it 
    #https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
    # Using __init__ as the contsructor of the class Player instead of using clean_data.
    def __init__(self, plyr):
        self.name = plyr["name"]
        self.guardians = plyr["guardians"].split(" and ")
        self.experience = True if plyr["experience"] == "YES" else False
        self.height = int(plyr["height"][: 2])
    #converts the object into a string
    #https://realpython.com/lessons/how-and-when-use-__str__/
    def __str__(self):
        return self.name


class Team:
    experienced = 0
    inexperienced = 0
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.height_average = sum([plyr.height for plyr in self.players])/len(self.players)
        self.experienced += sum([1 for plyr in self.players if plyr.experience])
        self.inexperienced += sum([1 for plyr in self.players if not plyr.experience])
        self.guardians = ", ".join([guard for plyr in self.players for guard in plyr.guardians])

    # Displaying the stats in a string
    def __str__(self):
        return """
        
Team {} stats\n
-------------------\n
Total Players: {}
Experienced Players: {}
Inexperienced Players: {}
Average height: {}
\nList of players:
  {}
\nList of guardians:
  {}
\n-------------------
        """.format(
            self.name,
            len(self.players),
            self.experienced,
            self.inexperienced,
            self.height_average,
            ", ".join([str(plyr) for plyr in self.players]),
            self.guardians)


def balance_teams(teams, players):
    #Creates the Player object and adds it to a list
    list_of_players = [Player(plyr) for plyr in players]
    experienced_players = []
    inexperienced_players = []
    team_players = []

    #Divides the players by experience
    for player in list_of_players:
        if player.experience:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    
    #Distributes evenly the inexperienced and experienced players
    for i in range(0, len(experienced_players)-1, len(teams)):
        team_players.append(Team(teams[int(i /len(teams))],
        experienced_players[i:i+int(len(experienced_players)/len(teams))] +
        inexperienced_players[i:i+int(len(inexperienced_players)/len(teams))]))
        
    return team_players


if __name__ == "__main__":
    app_running = True
    teams = balance_teams(constants.TEAMS, constants.PLAYERS)
    while app_running:
        print("\nBASTKETBALL TEAM STATS TOOL\n \n---- MENU ----\n\n Here are your choices:\n   1) Display Team Stats\n   2) Quit\n\n")
        command = input("Enter an option: ")
        if command == "1":
            print("\nShow The Stats\n\n--------------------\n\n1) Panthers\n2) Bandits\n3) Warriors\n\n")
            team_name = input("Enter an option (1, 2 or 3): ")
            try:
                print(teams[int(team_name) - 1])
                input("Press enter to continue...")
            except (ValueError, IndexError) as err:
                print("{}. Please enter numbers 1, 2, or 3 to show the team stats. Thank you.".format(err))
                input("Press Enter to continue... ")

        elif command == "2":
            app_running = False
        else:
            print("You entered {}, please enter 1 to display the team stats or 2 to quit the program. Thank you. ".format(command))
            input("Press Enter to continue... ")
    
