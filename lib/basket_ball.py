from lib.basket_ball import *

def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }
    
def num_points_per_game(game_dict):
    # Extract the "home" and "away" team data
    teams = ["home", "away"]
    points_per_game = {}

    # The loop below will extract the points_per_game for each player in each team
    for team in teams:
        for player in game_dict[team]["players"]:
            points_per_game[player["name"]] = player["points_per_game"]
    
    return points_per_game
# This function will return the age of a player
def player_age(player):
    return player["age"]
# This function will return the height of a player
def team_colors(team):
    return team["colors"]
# This function will return the name of a team
def team_name(team):
    return team["team_name"]
# This function will return the stats of a player
def player_stats(player_name):
    data = game_dict()
    # Search for the player in both teams
    for team in data.values():
        for player in team["players"]:
            if player["name"] == player_name:
                return player
                
    # If player is not found, return None
    return None

# This function will return the number of a player
def player_number(player):
    return player["number"]

def average_rebounds_by_shoe_brand():
    # This dictionary will store the average rebounds per shoe brand
    shoe_brands_rebounds = {}
    
    # Get the game data
    data = game_dict()
    
    # Iterate through both home and away teams
    for team in data.values():
        for player in team["players"]:
            brand = player["shoe_brand"]
            rebounds = player["rebounds_per_game"]
            
            # He we haven't seen this brand before, create an empty list
            if brand not in shoe_brands_rebounds:
                shoe_brands_rebounds[brand] = []
            
            # Append the player's rebounds to the appropriate brand list
            shoe_brands_rebounds[brand].append(rebounds)
    
    # Here we calculate the average rebounds per shoe brand
    for brand, rebounds_list in shoe_brands_rebounds.items():
        average_rebounds = sum(rebounds_list) / len(rebounds_list)
        print(f"{brand}: {average_rebounds:.2f}")
        
def player_with_most_career_points():
    data = game_dict()
    max_points = 0
    player_with_max_points = None
    
    for team in data.values():
        for player in team["players"]:
            if player["career_points"] > max_points:
                max_points = player["career_points"]
                player_with_max_points = player["name"]
                
    return player_with_max_points, max_points

# Example usage
print(player_with_most_career_points())

def jersey_numbers_worn_by_both_teams():
    data = game_dict()
    home_team_numbers = set()
    away_team_numbers = set()
    
    for player in data["home"]["players"]:
        home_team_numbers.add(player["number"])
    
    for player in data["away"]["players"]:
        away_team_numbers.add(player["number"])
    
    common_numbers = home_team_numbers.intersection(away_team_numbers)
    
    return common_numbers

# Example usage
print(jersey_numbers_worn_by_both_teams())

def player_with_longest_name():
    data = game_dict()
    longest_name_length = 0
    player_with_longest_name = None
    
    for team in data.values():
        for player in team["players"]:
            if len(player["name"]) > longest_name_length:
                longest_name_length = len(player["name"])
                player_with_longest_name = player["name"]
                
    return player_with_longest_name, longest_name_length

# Example usage
print(player_with_longest_name())


print("***************************")
print(num_points_per_game(game_dict()))
print(team_colors(game_dict()["home"]))
print(team_name(game_dict()["home"]))
print(player_number(player_stats("Darius Garland")))
print(player_stats("Darius Garland"))
print(average_rebounds_by_shoe_brand())
print(player_with_most_career_points())
print(jersey_numbers_worn_by_both_teams())
print(player_with_longest_name())
print("***************************")

