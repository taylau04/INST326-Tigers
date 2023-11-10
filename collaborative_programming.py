"""This is our collaborative programming exercise."""

"""This is my edit haha hehe - Richmond Akondo"""

"""This is Taylor's edit woooo"""

""" This is my docstring!!! - Sam """

""" This is my docstring! - Aadarsh """
 
""" rene made this - rene """

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class CollegeBasketballPlayer:
    
    def __init__(self, name):
        self.scores = []
        self.name = name
        
    def add_score(self, score):
        self.scores.append(score)
    
    def performance_graph(self):
        """
        Generates a performance graph for the given player, displaying the scores
        across multiple games.

        Args:
        - self: An instance of the class containing player information.

        The function creates a DataFrame from the player's scores, calculates 
        the average score, and then generates a bar plot using seaborn.
        It also adds a dashed line indicating the average score and annotates
        it with the average value. The x-axis represents the games, 
        and the y-axis represents the scores.

        Side efects: 
            Plots a bar chart on the screen
        
        Returns:
            None
        """
        df = pd.DataFrame({'Score': self.scores,
                           'Game': range(1, len(self.scores) + 1)})

        # Calculate the average score.
        average_score = df['Score'].mean()

        # Plot the bar using seaborn
        sns.barplot(x='Game', y='Score', data=df)

        # Add a horizontal line for the average score using Matplotlib.
        plt.axhline(average_score, color='black', linestyle='dashed',
                    linewidth=2)

        # Annotate the average line.
        plt.text(len(self.scores)-1, average_score,
                 f'Average: {average_score:.1f}',
                color='red', va='top', ha='right')

        # Adding labels and title
        plt.xlabel(f'Games')
        plt.ylabel('Score')
        plt.title(f'Scores of {self.name} for multiple games')

        # Display the plot.
        plt.show()



class BasketballPlayer:
    """
    Represents a basketball player's performance in a game.
    
    Attributes:
        name (str): The name of the player.
        points (int): Points scored by the player.
        assists (int): Number of assists made by the player.
        rebounds (int): Number of rebounds made by the player.
        steals (int): Number of steals made by the player.
        blocks (int): Number of blocks made by the player.
        turnovers (int): Number of turnovers committed by the player.
    """

    def __init__(self, name, points, assists, rebounds, steals, blocks, turnovers):
        """
        Initializes a new BasketballPlayer instance with given statistics.

        Args:
            name (str): The name of the player.
            points (int): Points scored by the player.
            assists (int): Number of assists made by the player.
            rebounds (int): Number of rebounds made by the player.
            steals (int): Number of steals made by the player.
            blocks (int): Number of blocks made by the player.
            turnovers (int): Number of turnovers committed by the player.
        """
        self.name = name
        self.points = points
        self.assists = assists
        self.rebounds = rebounds
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers

    def calculate_performance_score(self):
        """
        Calculates the performance score of the player based on their statistics.

        The performance score is a weighted sum of various statistics like points,
        assists, rebounds, etc., each having a different impact on the score.

        Returns:
            float: The calculated performance score.
        """
        # Weights for each stat - these can be adjusted
        weights = {
            'points': 0.2,
            'assists': 0.15,
            'rebounds': 0.15,
            'steals': 0.1,
            'blocks': 0.1,
            'turnovers': -0.2  # Negative weight for turnovers
        }

    def player_comparison(f, player_name1, player_name2):
        """Open, reads the file, and iterates over each line.

        Args:
            f(str): the file name
            player_name1(str): the 1st player's name and stats
            player_name2(str): the 2nd player's name and stats

        Returns:
            Returns both player's statistics from the txt file and states
            which player has the highest rating

        """
        with open(f, "r", encoding="utf-8") as f:
            for line in f:
                lines = line.strip().split()
                # not sure how the txt file will be formatting the statistics of each player
                # code underneath will be subject to change depending on the txt file
                if lines == player_name1:
                    print(player_name1)
                elif lines == player_name2:
                    print(player_name2)