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

class BasketballPlayer:
    """
    Represents a basketball player and tracks their game statistics.
    
    Attributes:
        name (str): The name of the player.
        stats (dict): A dictionary to store the player's game statistics.
    """

    def __init__(self, name):
        """
        Initializes a new BasketballPlayer instance with a given name.

        Args:
            name (str): The name of the basketball player.
        """
        self.name = name
        self.stats = {'points': 0, 'assists': 0, 'rebounds': 0, 
                      'steals': 0, 'blocks': 0, 'turnovers': 0}
    
def get_player1_stats(filepath):
        """Open, reads the file, and iterates over each line.

        Args:
            f(str): the file name

        Returns:
            Returns both player's statistics from the txt file and states
            which player has the highest rating

        """
        name1 = input("Input player 1: ")
        with open(filepath, "r", encoding="utf-8") as f:
            read_csv = csv.reader(f)
            column_names = next(read_csv)
            for line in read_csv:
                if line[0] == name1:
                    return line

def get_player2_stats(filepath, name2):
        """Open, reads the file, and iterates over each line.

        Args:
            f(str): the file name

        Returns:
            Returns both player's statistics from the txt file and states
            which player has the highest rating

        """
        name2 = input("Input player 1: ")
        with open(filepath, "r", encoding="utf-8") as f:
            read_csv = csv.reader(f)
            column_names = next(read_csv)
            for line in read_csv:
                if line[0] == name2:
                    return line


    def add_stats(self, points=0, assists=0, rebounds=0, 
                  steals=0, blocks=0, turnovers=0):
        """
        Adds or updates the player's game statistics.

        Args:
            points (int): Points scored by the player.
            assists (int): Number of assists made by the player.
            rebounds (int): Number of rebounds made by the player.
            steals (int): Number of steals made by the player.
            blocks (int): Number of blocks made by the player.
            turnovers (int): Number of turnovers committed by the player.
        """
        self.stats['points'] += points
        self.stats['assists'] += assists
        self.stats['rebounds'] += rebounds
        self.stats['steals'] += steals
        self.stats['blocks'] += blocks
        self.stats['turnovers'] += turnovers

    def calculate_performance_score(self):
        """
        Calculates a performance score for the player based on their statistics.

        The performance score is a weighted sum of the player's stats,
        where each stat category has a specific weight.

        Returns:
            float: The calculated performance score, constrained between 0 and 100.
        """
        weights = {'points': 2.5, 'assists': 2.0, 'rebounds': 1.5, 
                   'steals': 3.0, 'blocks': 3.0, 'turnovers': -2.0}
        score = sum(self.stats[stat] * weights[stat] for stat in self.stats)
        return min(max(score, 0), 100)

    def get_grade(self, score):
        """
        Determines the grade of the player based on their performance score.

        Args:
            score (float): The performance score of the player.

        Returns:
            str: The grade (A, B, C, D, or F) based on the performance score.
        """
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

def get_stat_input(stat_name):
    """
    Prompts the user to input a statistical value for a given stat category.

    Args:
        stat_name (str): The name of the stat category for which the value is being input.

    Returns:
        int: The input value for the stat.
    """
    while True:
        try:
            return int(input(f"Enter {stat_name}: "))
        except ValueError:
            print("Please enter a valid integer.")

player_name = input("Enter the player's name: ")
player = BasketballPlayer(player_name)

player.add_stats(
    points=get_stat_input("points"),
    assists=get_stat_input("assists"),
    rebounds=get_stat_input("rebounds"),
    steals=get_stat_input("steals"),
    blocks=get_stat_input("blocks"),
    turnovers=get_stat_input("turnovers")
)

performance_score = player.calculate_performance_score()
grade = player.get_grade(performance_score)
print(f"Performance Score for {player.name}: {performance_score:.2f} (Grade: {grade})")

    def __repr__(self):
        return f"BasketballPlayer(name = '{self.name}', points = '{self.points}', assists = '{self.assists}', steals = '{self.steals}, turnovers = '{self.turnovers}')"
        
                    

    def searchStats(category, operator, number):
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
        
        with open(file, "r", encoding="utf-8") as file:
            for line in file:
                line.strip.split()

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
                
                
        
    