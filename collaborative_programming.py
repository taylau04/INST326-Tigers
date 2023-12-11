"""
"""
from argparse import ArgumentParser
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
        """Primary Author: Taylor Lau w/ assistance from Rene
           Techniques used: with statements
           
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
        """ Primary Author: Taylor Lau
            Techniques used: Conditional expressions
        
        This function compares the scaled score of player 1 and player 2.
        
        Args:
            player1_name (str): name of player 1.
            player2_name(str): name of player 2.
            score1 (float): the scaled score of player 1.
            score2 (float): the scaled score of player 2.
        
        Returns:
            Returns f-strings which describing if player 1 had a higher or lower score than player 2.
        """
        return(
            f"{player1_name} received a higher performance score than {player2_name}"
            if score1 > score2 else
            (f"{player2_name} received a higher performance score than {player1_name}"
            if score1 < score2 else
            f"{player1_name} is the same performance score as {player2_name}")
        )

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
        
        # Created a list of possible categories
        self.possible_categories = ["Pos", "Age", "GS", "MP","FG%",
                                    "FT%",
                                    "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
        
        filepath = "/Users/richmondo/Desktop/NBA_2024_per_game(15-11-2023 Updated).csv"

        self.operator = operator
        self.category = category
        self.number = number

        df = pd.read_csv(filepath)

        # Checking if the provided category is in the list of possible categories
        if self.category not in self.possible_categories:
            raise ValueError("Invalid category. Choose from: {}".format(", ".join(self.possible_categories)))

        # Defining the condition based on the operator
        if self.operator == '>':
            condition = df[self.category] > number
        elif self.operator == '<':
            condition = df[self.category] < number
        elif self.operator == '=':
            condition = df[self.category] == number
        else:
            raise ValueError("Invalid operator. Use '>', '<', or '='.")

        # Using boolean indexing to filter the DataFrame
        result_df = df[condition]

        # Converting the result to a list of dictionaries
        result_list = result_df.to_dict('records')

        return result_list

    def __call__(self, reverse=False):
        # Prompting the user for input on category, number, and operator
        category = input("What category would you like to view? ")
        number = float(input("Enter the number: "))
        operator = input("Enter the operator ('>', '<', '='): ")

        # Checking if the provided category is in the list of possible categories
        if category not in self.possible_categories:
            raise ValueError("Invalid category. Choose from: {}".format(", ".join(self.possible_categories)))

        result_list = self.searchStats(operator, category, number)

        # Setting the sort_key to the specified category
        sort_key = category

        result_list.sort(key=lambda x: x[sort_key], reverse=reverse)

        return result_list
    
    # Testing
    # Creating an instance of the class
# nba_search = PlayerGrader()

    # Searching and sorting by the specified category in descending order
# result = PlayerGrader(reverse=True)
# print(result)


    def show_best_performing_teams(self, criteria_column, 
                                   number_of_best_teams=None):
        """
        Read a dataset from a CSV file and return the best performing teams 
        based on a given criteria.

        Args:
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
        df = pd.read_csv(self.filepath)
        grouped_by_team = df.groupby("Tm")[criteria_column]
        average_by_team = grouped_by_team.sum()
        sorted_by_average = average_by_team.sort_values(key=lambda x: -1 * x)
        if number_of_best_teams is None:
            return sorted_by_average
        return sorted_by_average[:number_of_best_teams]

    def show_player_stats_by_team_barplot(self, team_name, stats_column):
        """
        Generate a bar plot showing the specified basketball statistics for 
        each player in a given team.

        Args:
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
        df = pd.read_csv(self.filepath)
        plot_data = df[df["Tm"] == team_name][["Player", stats_column]]

        sns.barplot(x='Player', y=stats_column, hue='Player', data=plot_data)

        plt.title(f'{stats_column_desc} per Player of {team_name}')
        plt.xlabel('Player')
        plt.ylabel(f'{stats_column_desc} ({stats_column})')
        plt.xticks(rotation=45, ha='right')  # Rotate the player names
        plt.subplots_adjust(bottom=0.3)  # Adjust the bottom margin
        plt.show()

def main(arguments):
    """Main function to initiate the player grading process.

    This function creates an instance of the PlayerGrader class, fetches stats
    for two players entered by the user, calculates their grades, and prints the results.
    """

    filepath = arguments.file
    grader = PlayerGrader(filepath)

    if arguments.action == "compare_players":
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
        return
    
    if arguments.action == "show_best_teams":
        print("Enter statistic name to evaluate")
        print("Valid values are: ")
        for code, name in basketball_stats_dict.items():
            if code in ["Player", "Pos", "Age", "Tm"]:
                continue
            print(f"    {code}: {name}")
        criteria_column = input("Enter one of the statistic abbreviations: ")
        if criteria_column not in basketball_stats_dict:
            print(f"Invalid statistic name {criteria_column}")
            return
        no_best_teams = input("Enter number of teams to show (default is all): ")
        if no_best_teams.strip() == "":
            no_best_teams = None
        else:
            no_best_teams = int(no_best_teams.strip())
        teams = grader.show_best_performing_teams(criteria_column, number_of_best_teams=no_best_teams)
        print(f"The best performing teams for statistic {criteria_column} are:")
        teams_df = pd.DataFrame(teams).reset_index()
        teams_df.columns = ["Team", basketball_stats_dict[criteria_column]]
        print(teams_df)
        return
    
    if arguments.action == "player_stats_by_team":
        team_name = input("Enter team name: ")
        print("Enter statistic name to evaluate")
        print("Valid values are: ")
        for code, name in basketball_stats_dict.items():
            if code in ["Player", "Pos", "Age", "Tm"]:
                continue
            print(f"    {code}: {name}")
        stats_column = input("Enter one of the statistic abbreviations: ")
        if stats_column not in basketball_stats_dict:
            print(f"Invalid statistic name {stats_column}")
            return
        grader.show_player_stats_by_team_barplot(team_name, stats_column)
        return

    if arguments.action == "search_stats":
        result_list = grader.searchStats(input("Enter category: "), 
                                         input("Enter operator ('>', '<', '='): "), 
                                         float(input("Enter number: ")))
        print(result_list)

    if arguments.action == "call_method":
        result_list = grader(reverse=True)
        print(result_list)

    
def parse_args():
    """Parse and validate command-line arguments.

    Returns:
        namespace: the parsed arguments, as a namespace. 
    """
    parser = ArgumentParser()
    parser.add_argument('file', type=str, help='Path to the file containing player statistics')
    parser.add_argument('action', type=str, 
                        help='Name of the action to run: ' 
                        'compare_players | show_best_teams | player_stats_by_team | search_stats | call_method')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(args)
