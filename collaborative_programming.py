"""This is our collaborative programming exercise."""

"""This is my edit haha hehe - Richmond Akondo"""

"""This is Taylor's edit woooo"""

""" This is my docstring!!! - Sam """

""" This is my docstring! - Aadarsh """
 
""" rene made this - rene """

import seaborn as sns
import matplotlib.pyplot as plt
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

def main():
    """
    Main function to initiate the player grading process.

    This function creates an instance of the PlayerGrader class, fetches stats
    for two players entered by the user, calculates their grades, and prints the results.
    """
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



    def searchStats(self, category, operator, number):
        """This function’s purpose is to be a search tool for users to search 
            for specific stats to see which players fit in to the category 
            being searched

        Args:
            category (string): This string can be any category in the stat line 
            of a specific player from ppg (points per game), to 3pt%, to free 
            throw %
            operator (string): this will either be >, <, or = determining 
            whether the user wants a stat greater than, less than, or equal to
            the number
            number (int): This is a number for a specific stat line. For example
            25 could represent a 25 ppg
        Returns:
            List: A list of players in the file that match the catgeory being 
            searched    
        """
        
        filepath = ("N:Users:richmondo:Downloads:archive (1):NBA_2024_per_game(13-11-2023 Updated).csvBA_2024_per_game(13-11-2023 Updated).csv")
    
        self.operator = operator
        self.category = category
        self.number = number
    
        df = pd.read_csv(filepath)

        # Defining the condition based on the operator
        if operator == '>':
            condition = df[category] > number
        elif operator == '<':
            condition = df[category] < number
        elif operator == '=':
            condition = df[category] == number
        else:
            raise ValueError("Invalid operator. Use '>', '<', or '='.")

        #Using boolean indexing to filter the DataFrame
        result_df = df[condition]

        #Converting the result to a list of dictionaries
        result_list = result_df.to_dict('records')

        return result_list
    
    def __call__(self, operator, category, number, sort_key=None, reverse=False):
        result_list = self.searchStats(operator, category, number)

        if sort_key:
            result_list.sort(key=lambda x: x[sort_key], reverse=reverse)

        return result_list

    def show_best_performing_teams(self, filepath, criteria_column, 
                                   number_of_best_teams=None):
        """
        Read a dataset from a CSV file and return the best performing teams 
        based on a given criteria.

        Args:
        - filepath (str): The path to the CSV file containing the dataset.
        - criteria_column (str): The name of the column in the dataset that is 
        used to evaluate team performance.
        - number_of_best_teams (int): The number of top-performing teams to 
        return.

        Returns:
        pandas.Series: A series with team names as the index and their
        average performance metric as values, sorted in descending order of 
        performance.

        The function performs the following steps:
        1. Reads the dataset from the specified CSV file into a Pandas 
        DataFrame.
        2. Groups the data by the 'Tm' (team) column and calculates the mean of 
        the specified criteria column for each team.
        3. Sorts the teams by their average performance in descending order.
        4. Returns the specified number of top-performing teams.
        """
        df = pd.read_csv(filepath)
        grouped_by_team = df.groupby("Tm")[criteria_column]
        average_by_team = grouped_by_team.sum()
        sorted_by_average = average_by_team.sort_values(key=lambda x: -1 * x)
        if number_of_best_teams is None:
            return sorted_by_average
        return sorted_by_average[:number_of_best_teams]

    def show_player_stats_by_team_barplot(self, filepath, team_name, 
                                          stats_column):
        """
        Generate a bar plot showing the specified basketball statistics for 
        each player in a given team.

        Args:
        - filepath (str): Path to the CSV file containing the basketball 
        statistics data.
        - team_name (str): Name of the team for which the statistics are to be 
        plotted.
        - stats_column (str): The specific column/statistic to be plotted 
        (e.g., 'PTS' for points per game).

        This function reads the basketball data from the specified CSV file, 
        filters it for a given team, and creates a bar plot for a specific 
        statistical column. The plot displays each player on the x-axis and 
        their respective statistic on the y-axis.

        Note:
        - The function does not plot statistics for non-numerical columns like 
        'Player', 'Tm', and 'Pos'.
        - The function relies on a pre-defined dictionary 'basketball_stats_dict' 
        for column descriptions.

        The function first checks if the specified statistical column is
        valid and can be plotted.
        If valid, it then filters the DataFrame for the specified team, 
        creates a bar plot, and displays it.
        """
        if stats_column in ["Player", "Tm", "Pos"]:
            print(f"Cannot plot statistics for column {stats_column}")
            return
        stats_column_desc = basketball_stats_dict.get(stats_column)
        if stats_column_desc is None:
            print(f"Cannot plot statistics for column {stats_column}," 
                  " no such statistics available.")
            return
        df = pd.read_csv(filepath)
        plot_data = df[df["Tm"] == team_name][["Player", stats_column]]

        sns.barplot(x='Player', y=stats_column, data=plot_data)

        plt.title(f'{stats_column_desc} per Player')
        plt.xlabel('Player')
        plt.ylabel(f'{stats_column_desc} ({stats_column})')
        plt.xticks(rotation=90)  # Rotate the player names
        plt.show()

def main():
    """Main function to run the basketball player statistics analyzer.

    Returns:
        None
       """
    # Parse command-line arguments
    args = parse_args()
    # Perform player comparison
    player_comparison(args.file, args.player1, args.player2)

    # Example for the performance graph )
    player = CollegeBasketballPlayer("Player1")
    player.add_score(14) # will eventually replace with actual data
    player.add_score(26)
    player.performance_graph()

def parse_args(args):
    """Parse and validate command-line arguments.

    Returns:
        namespace: the parsed arguments, as a namespace. 
    """
    parser = ArgumentParser()
    parser.add_argument('file', type=str, help='Path to the file containing player statistics')
    parser.add_argument('player1', type=str, help='Name of the first player')
    parser.add_argument('player2', type=str, help='Name of the second player')
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.args[1:])
    main(args.file)           
                
                
        
    