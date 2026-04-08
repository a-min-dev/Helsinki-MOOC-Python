"""
The following program builds an application for examining NHL hockey 
statistics from the 2019-2020 season.  The program works with JSON files,
in which each entry for a player includes such information as a player's
name, nationality, team, and goals made during the season.

A user can use the application to review statistics by selecting a command,
such as searching by player, team, finding the player with the most goals,
and other commands.
"""

import json

class Player:
    """The class represents a single NHL player and his season-long stats"""
    def __init__(self, name: str, team: str, nationality: str, assists: int, goals: int, games: int):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.assists = assists
        self.games = games
        self.goals = goals

    @property
    def points(self):
        """Calculate the total points for a player, which is the sum of goals and assists"""
        return self.assists + self.goals

    def __str__(self):
        """Return a formatted string for an aligned output to the console"""
        return f"{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {self.points:3}"


class PlayerStats:
    """The class manages player data, searching, and logic for sorting"""
    def __init__(self, filename: str):
        self.players = []
        self.load_data(filename)

    def load_data(self, filename: str):
        """Populate the self.players list with Player objects from a JSON file"""
        with open(filename) as my_file:
            players_data = json.load(my_file)

        for player in players_data:
            # Create instances of the Player class for each dictionary in the JSON file
            new_player = Player(player["name"], player["team"], player["nationality"], player["assists"], player["goals"], player["games"])
            self.players.append(new_player)

    def get_player(self, name: str):
        """Search for a specific player by name"""
        for player in self.players:
            if player.name == name:
                return player

        return None

    def get_teams(self):
        """Return a sorted list of unique 3-letter team abbreviations"""
        teams = []
        for player in self.players:
            teams.append(player.team)
        return sorted(list(set(teams)))

    def get_countries(self):
        """Using list comprehension, return a set of sorted, unique 3-letter country codes"""
        return sorted(list(set(player.nationality for player in self.players)))

    def players_on_team(self, team: str):
        """Filter players by team, then sort the players in descending order by points"""
        subset = [player for player in self.players if player.team == team]
        subset.sort(key = lambda player: player.points, reverse = True)

        return subset

    def players_from_country(self, country: str):
        """Filter players by country, then sort the players in descending order by points"""
        subset = [player for player in self.players if player.nationality == country]
        subset.sort(key = lambda player: player.goals + player.assists, reverse = True)

        return subset

    def top_scorers(self, n: int):
        """Return top n players by total points, where ties are broken by goals scored"""
        sorted_players = sorted(self.players, 
                                key = lambda player: (player.points, player.goals),
                                reverse = True)

        return sorted_players[:n]

    def top_goal_scorers(self, n: int):
        """Return top n players by goals scored, where ties are broken by fewer games played"""
        # -player.games allows to flip the direction for games played to properly sort by fewer games played
        sorted_players = sorted(self.players,
                                key = lambda player: (player.goals, -player.games),
                                reverse = True)
        
        return sorted_players[:n]

def main():
    """A main function to handle user interface and the command processing loop"""
    filename = input("file name: ")
    stats = PlayerStats(filename)

    count = len(stats.players)

    print(f"read the data of {count} players")
    print("commands: ")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")

    while True:
        command = input("command: ")

        if command == "0":
            break

        elif command == "1":
            name = input("name: ")
            player = stats.get_player(name)
            if player:
                print(player)

        elif command == "2":
            teams = stats.get_teams()
            for team in teams:
                print(team)

        elif command == "3":
            countries = stats.get_countries()
            for country in countries:
                print(country)

        elif command == "4":
            team = input("team: ")
            players = stats.players_on_team(team)
            for player in players:
                print(player)

        elif command == "5":
            country = input("country: ")
            players = stats.players_from_country(country)
            for player in players:
                print(player)

        elif command == "6":
            num = int(input("how many: "))
            for player in stats.top_scorers(num):
                print(player)

        elif command == "7":
            num = int(input("how many: "))
            for player in stats.top_goal_scorers(num):
                print(player)

if __name__ == "__main__":
    main()