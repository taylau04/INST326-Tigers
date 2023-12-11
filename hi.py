#import seaborn as sns
#import matplotlib.pyplot as plt
import pandas as pd
import csv

basketball_stats_dict = {
    "Player": "Player's name",
    "Pos": "Position",
    "Age": "Player's age",
    "Tm": "Team",
    "G": "Games played",
    "GS": "Games started",
    "MP": "Minutes played per game",
    "FG": "Field goals per game",
    "FGA": "Field goal attempts per game",
    "FG%": "Field goal percentage",
    "3P": "3-point field goals per game",
    "3PA": "3-point field goal attempts per game",
    "3P%": "3-point field goal percentage",
    "2P": "2-point field goals per game",
    "2PA": "2-point field goal attempts per game",
    "2P%": "2-point field goal percentage",
    "eFG%": "Effective field goal percentage",
    "FT": "Free throws per game",
    "FTA": "Free throw attempts per game",
    "FT%": "Free throw percentage",
    "ORB": "Offensive rebounds per game",
    "DRB": "Defensive rebounds per game",
    "TRB": "Total rebounds per game",
    "AST": "Assists per game",
    "STL": "Steals per game",
    "BLK": "Blocks per game",
    "TOV": "Turnovers per game",
    "PF": "Personal fouls per game",
    "PTS": "Points per game"
}

class PlayerGrader:
    """
    A class to grade basketball players based on their statistics.

    This class reads player statistics from a CSV file and calculates a grade
    for each player based on a weighted evaluation of their performance.

    Attributes:
        filepath (str): The file path to the CSV file containing player stats.
    """

    def __init__(self, filepath):
        """
        Initializes the PlayerGrader with the path to the CSV file.

        Args:
            filepath (str): The file path to the CSV file containing player stats.
        """
        self.filepath = filepath
    
    def menu():
        menu_options = {1: "Get player stats", 2: "Team stat Data Visualization", 3: "Search stat"}
        while True:
            print(menu_options)
            user_input = input("Pick a number: ")
            break
            if user_input == 1:
                PlayerGrader.get_player_stats(player_name)
                PlayerGrader.calculate_player_grade(player_stats)
                PlayerGrader.player_comparison(player1_name, player2_name, score1, score2)
            elif user_input == 2:
                show_best_performing_teams(filepath, criteria_column,number_of_best_teams=None)
                show_player_stats_by_team_barplot(filepath, team_name, stats_column)
                continue
            elif user_input == 3:
                searchStats(category, operator, number)
            else:
                print("Not a Valid Choice")
                    

    def get_player_stats(self, player_name):
        """
        Retrieves the statistics for a specific player from the CSV file.

        Args:
            player_name (str): The name of the player whose stats are to be retrieved.

        Returns:
            pd.Series: A pandas Series containing the player's statistics. Returns
            None if the player is not found in the file.
        """
        with open(self.filepath, "r", encoding="utf-8") as f:
            read_csv = csv.reader(f)
            column_names = next(read_csv)
            for line in read_csv:
                if line[0].lower() == player_name.lower():
                    stats = {stat: float(line[column_names.index(stat)]) for stat in ['PTS', 'AST', 'TRB', 'STL', 'BLK', 'TOV']}
                    return pd.Series(stats)
        return None

    def calculate_player_grade(self, player_stats):
        """
        Calculates the grade of a player based on their statistics.

        The function uses a weighted scoring system for different statistics
        (like points, assists, rebounds, etc.) and then converts this score into a letter grade.

        Args:
            player_stats (pd.Series): A pandas Series containing player's statistics.

        Returns:
            tuple: A tuple containing the letter grade (str) and numeric score (float) for the player.
        """
        weights = {'PTS': 1.1, 'AST': 1.05, 'TRB': 1.05, 'STL': 1.1, 'BLK': 1.1, 'TOV': -0.9}
        total_score = sum([player_stats[stat] * weights[stat] for stat in weights])
        scaled_score = max(0, min(100, total_score * 2))

        if scaled_score >= 96.5:
            grade = 'A+'
        elif scaled_score >= 92.5:
            grade = 'A'
        elif scaled_score >= 89.5:
            grade = 'A-'
        elif scaled_score >= 86.5:
            grade = 'B+'
        elif scaled_score >= 82.5:
            grade = 'B'
        elif scaled_score >= 79.5:
            grade = 'B-'
        elif scaled_score >= 76.5:
            grade = 'C+'
        elif scaled_score >= 72.5:
            grade = 'C'
        elif scaled_score >= 69.5:
            grade = 'C-'
        elif scaled_score >= 66.5:
            grade = 'D+'
        elif scaled_score >= 62.5:
            grade = 'D'
        elif scaled_score >= 59.5:
            grade = 'D-'
        else:
            grade = 'F'
        return grade, scaled_score

    def player_comparison(player1_name, player2_name, score1, score2):
        return(
            f"{player1_name} received a higher performance score than {player2_name}"
            if score1 > score2 else
            (f"{player2_name} received a higher performance score than {player1_name}"
            if score1 < score2 else
            f"{player1_name} is the same performance score as {player2_name}")
        )


def main():
    """
    Main function to initiate the player grading process.

    This function creates an instance of the PlayerGrader class, fetches stats
    for two players entered by the user, calculates their grades, and prints the results.
    """
    menu_options = PlayerGrader.menu()
    print(menu_options)
    
    
    filepath = "NBA_2024_per_game(28-11-2023).csv"
    grader = PlayerGrader(filepath)

    player1_name = input("Enter Player 1's name: ")
    player1_stats = grader.get_player_stats(player1_name)
    if player1_stats is not None:
        grade1, score1 = grader.calculate_player_grade(player1_stats)
        print(f"Player 1 Grade: {grade1}, Numeric Score: {score1}")
    else:
        print(f"No player found with the name '{player1_name}'.")

    player2_name = input("Enter Player 2's name: ")
    player2_stats = grader.get_player_stats(player2_name)
    if player2_stats is not None:
        grade2, score2 = grader.calculate_player_grade(player2_stats)
        print(f"Player 2 Grade: {grade2}, Numeric Score: {score2}")
    else:
        print(f"No player found with the name '{player2_name}'.")

    comparison = PlayerGrader.player_comparison(player1_name, player2_name, score1, score2)
    print(comparison)

if __name__ == "__main__":
    main()