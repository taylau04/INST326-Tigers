# INST326-Tigers

Example Runs:

```
Enter the following line below into the terminal to understand the usage of command line arguments.
python3 player_performance.py -h

usage: player_performance.py [-h] file action

positional arguments:
  file        Path to the file containing player statistics
  action      Name of the action to run: compare_players | show_best_teams | player_stats_by_team

options:
  -h, --help  show this help message and exit

```
```
Enter the following line below into the terminal to run __str__() methods. 
python3 player_performance.py NBA_2024_per_game\(28-11-2023\).csv stats

*Our program will ask the user to input a player's name. The following is an
example of the output

Enter player name: lebron james
PTS    25.5
AST     6.6
TRB     8.0
STL     1.5
BLK     0.8
TOV     3.8
```
```
Enter the following line below into the terminal to run get_player_stats(), calculate_player_grade(),
and player_comparison() methods. 
python3 player_performance.py NBA_2024_per_game\(28-11-2023\).csv compare_players

*Our program will ask the user to input player 1 and player 2's name. The following is an example 
of the output.

Enter Player 1's name: Lebron James
Player 1 Grade: B, Numeric Score: 84.98
Enter Player 2's name: Grayson Allen
Player 2 Grade: F, Numeric Score: 41.040000000000006
Lebron James received a higher performance score than Grayson Allen
```

```
Enter the following line below into the terminal to run show_best_performing_teams() method.
python3 player_performance.py NBA_2024_per_game\(28-11-2023\).csv show_best_teams

*Our program will ask the user to input a statistic and the number of teams to display 
within the df. The user must use an abbreviated statistic value and an integer for the 
number of teams. The following is an example of the output.

Enter statistic name to evaluate
Valid values are: 
    G: Games played
    GS: Games started
    MP: Minutes played per game
    FG: Field goals per game
    FGA: Field goal attempts per game
    FG%: Field goal percentage
    3P: 3-point field goals per game
    3PA: 3-point field goal attempts per game
    3P%: 3-point field goal percentage
    2P: 2-point field goals per game
    2PA: 2-point field goal attempts per game
    2P%: 2-point field goal percentage
    eFG%: Effective field goal percentage
    FT: Free throws per game
    FTA: Free throw attempts per game
    FT%: Free throw percentage
    ORB: Offensive rebounds per game
    DRB: Defensive rebounds per game
    TRB: Total rebounds per game
    AST: Assists per game
    STL: Steals per game
    BLK: Blocks per game
    TOV: Turnovers per game
    PF: Personal fouls per game
    PTS: Points per game
Enter one of the statistic abbreviations: DRB
Enter number of teams to show (default is all): 3
The best performing teams for statistic DRB are:
  Team  Defensive rebounds per game
0  BRK                         52.1
1  MIA                         51.2
2  LAC                         48.0
```

```
Enter the following line below into the terminal to run show_player_stats_by_team_barplot() method.
python3 player_performance.py NBA_2024_per_game\(28-11-2023\).csv player_stats_by_team

*Our program will ask the user to input a team name and a statistic value. The user 
must enter an abbreviation for both the team name and the statistic value. The following 
is an example of our output.

Enter team name: LAL
Enter statistic name to evaluate
Valid values are: 
    G: Games played
    GS: Games started
    MP: Minutes played per game
    FG: Field goals per game
    FGA: Field goal attempts per game
    FG%: Field goal percentage
    3P: 3-point field goals per game
    3PA: 3-point field goal attempts per game
    3P%: 3-point field goal percentage
    2P: 2-point field goals per game
    2PA: 2-point field goal attempts per game
    2P%: 2-point field goal percentage
    eFG%: Effective field goal percentage
    FT: Free throws per game
    FTA: Free throw attempts per game
    FT%: Free throw percentage
    ORB: Offensive rebounds per game
    DRB: Defensive rebounds per game
    TRB: Total rebounds per game
    AST: Assists per game
    STL: Steals per game
    BLK: Blocks per game
    TOV: Turnovers per game
    PF: Personal fouls per game
    PTS: Points per game
Enter one of the statistic abbreviations: PF
# A diagram shows up
```
```

Enter the following line below into the terminal to run the searchStats() method.
python3 player_performance.py NBA_2024_per_game\(28-11-2023\).csv search_stats

*Our program will ask the user to input a specific category of a player's stat line.
The user can input any of the following stats: "Pos", "Age", "GS", "MP","FG%",
"FT%","TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS". Then the user is asked for
an operator, and then a number. The following is an example 
of the output:

Enter Category: PTS
Enter operator ('>', '<', '='): >
Enter number: 20 

Output:
{'Player': 'Giannis Antetokounmpo', 'Pos': 'PF', 'Age': 29, 'Tm': 'MIL', 'G': 10, 'GS': 10, 'MP': 32.5, 'FG': 11.0, 'FGA': 18.9, 'FG%': 0.582, 'PTS': 29.5}
{'Player': 'Desmond Bane', 'Pos': 'SG', 'Age': 25, 'Tm': 'MEM', 'G': 10, 'GS': 10, 'MP': 35.4, 'FG': 9.8, 'FGA': 21.6, 'FG%': 0.454, 'PTS': 26.5}
{'Player': 'Stephen Curry', 'Pos': 'PG', 'Age': 35, 'Tm': 'GSW', 'G': 11, 'GS': 11, 'MP': 32.5, 'FG': 9.5, 'FGA': 19.5, 'FG%': 0.488, 'PTS': 25}
{'Player': 'Luka Dončić', 'Pos': 'PG', 'Age': 24, 'Tm': 'DAL', 'G': 10, 'GS': 10, 'MP': 35.8, 'FG': 11.2, 'FGA': 21.3, 'FG%': 0.526, 'PTS': 32}
{'Player': 'Kevin Durant', 'Pos': 'PF', 'Age': 35, 'Tm': 'PHO', 'G': 10, 'GS': 10, 'MP': 36.7, 'FG': 10.1, 'FGA': 20.3, 'FG%': 0.498, 'PTS': 21}
{'Player': 'Anthony Edwards', 'Pos': 'SG', 'Age': 22, 'Tm': 'MIN', 'G': 9, 'GS': 9, 'MP': 35.9, 'FG': 10.4, 'FGA': 21.4, 'FG%': 0.487, 'PTS': 27.4}
{'Player': 'Joel Embiid', 'Pos': 'C', 'Age': 29, 'Tm': 'PHI', 'G': 9, 'GS': 9, 'MP': 33.8, 'FG': 11.0, 'FGA': 21.8, 'FG%': 0.505, 'PTS': 23.5}
{'Player': "De'Aaron Fox", 'Pos': 'PG', 'Age': 26, 'Tm': 'SAC', 'G': 4, 'GS': 4, 'MP': 35.5, 'FG': 11.3, 'FGA': 22.5, 'FG%': 0.5, 'PTS': 27}
{'Player': 'Shai Gilgeous-Alexander', 'Pos': 'PG', 'Age': 25, 'Tm': 'OKC', 'G': 9, 'GS': 9, 'MP': 35.7, 'FG': 11.2, 'FGA': 21.3, 'FG%': 0.526, 'PTS': 23.3}
{'Player': 'LeBron James', 'Pos': 'PF', 'Age': 39, 'Tm': 'LAL', 'G': 9, 'GS': 9, 'MP': 35.0, 'FG': 9.7, 'FGA': 17.0, 'FG%': 0.569, 'PTS': 24.3}
{'Player': 'Nikola Jokić', 'Pos': 'C', 'Age': 28, 'Tm': 'DEN', 'G': 10, 'GS': 10, 'MP': 34.6, 'FG': 12.0, 'FGA': 19.8, 'FG%': 0.606, 'PTS': 26.8}
{'Player': 'Kyle Kuzma', 'Pos': 'PF', 'Age': 28, 'Tm': 'WAS', 'G': 10, 'GS': 10, 'MP': 30.3, 'FG': 9.6, 'FGA': 19.8, 'FG%': 0.485, 'PTS': 23.2}
{'Player': 'Lauri Markkanen', 'Pos': 'PF', 'Age': 26, 'Tm': 'UTA', 'G': 10, 'GS': 10, 'MP': 33.5, 'FG': 8.1, 'FGA': 16.7, 'FG%': 0.485, 'PTS': 27.8}
{'Player': 'Tyrese Maxey', 'Pos': 'PG', 'Age': 23, 'Tm': 'PHI', 'G': 9, 'GS': 9, 'MP': 37.9, 'FG': 10.3, 'FGA': 20.4, 'FG%': 0.505, 'PTS': 23.4}
{'Player': 'Donovan Mitchell', 'Pos': 'SG', 'Age': 27, 'Tm': 'CLE', 'G': 9, 'GS': 9, 'MP': 36.2, 'FG': 10.2, 'FGA': 21.8, 'FG%': 0.469, 'PTS': 22.3}
{'Player': 'Jayson Tatum', 'Pos': 'PF', 'Age': 25, 'Tm': 'BOS', 'G': 10, 'GS': 10, 'MP': 36.2, 'FG': 10.2, 'FGA': 19.4, 'FG%': 0.526, 'PTS': 24.3}
{'Player': 'Cam Thomas', 'Pos': 'SG', 'Age': 22, 'Tm': 'BRK', 'G': 8, 'GS': 7, 'MP': 32.4, 'FG': 9.9, 'FGA': 20.6, 'FG%': 0.479, 'PTS': 23.1}
{'Player': 'Trae Young', 'Pos': 'PG', 'Age': 25, 'Tm': 'ATL', 'G': 9, 'GS': 9, 'MP': 35.8, 'FG': 6.7, 'FGA': 18.7, 'FG%': 0.357, 'PTS': 26}

These are all players that score more than 20 points 

```
```
Interpretting output of the program 
Our program consists of three sections: comparing two NBA players (compare_players), displaying best 
NBA teams (show_best_teams), and data visualization of player stats (player_stats_by_team). 
* compare_players
  * The comparing two NBA players returns an output of the player 1 and player 2's grade and scaled score. 
  The method will then display which player has a higher score. 
* show_best_teams
  * This section will display a df of top teams based on a certain statistic that the user inputs. 
* player_stats_by_team 
  * This will output a data visualization consisting of players from a chosen NBA team and a chosen statistic 
  based on the user's input.

```

```
Attribution 
| Function/Method                     | Primary Author| Techniques Demonstrated     |
| ------------------------------------| ------------- |-------------------------    |
| show_player_stats_by_team_barplot() | Aadarsh       | Data Visualization          |
| show_best_performing_teams()        | Aadarsh       | Pandas                      |
| get_player_stats()                  | Taylor        | With Statements             |
| player_comparison()                 | Taylor        | Conditional Expressions     |
| calculate_player_grade()            | Rene          | Min/max & sorting           |
| calculate_player_grade()            | Rene          | List comprehensions         |
| __call__()                          | Richmond      | Magic Methods               |
| __call__()                          | Richmond      | Optional Parameters         |
| parse_args()                        | Samantha      | Argument Parser             |
| main()                              | Samantha      | f-strings                   |                
| ----------------------------------- | ------------- | ----------------------------

Primary Authors of each function 
* show_player_stats_by_team_barplot() and show_best_performing_teams() was created by Aadarsh
* get_player_stats() was created by Taylor with assistance by Rene
* player_comparison() was created by Taylor 
* __str__(), calculate_player_grade() was created by Rene 
* searchStats() and __call__() was created by Richmond 
* parse_args() was created by Samantha with assistance from Aadarsh
* main() was created by Samantha with assistance from Rene and Aadarsh
```
```
Files in Repository
* NBA_2024_per_game(28-11-2023).csv: A csv file consisting of stats from NBA players
* README.md: A markdown file consisting of documentation about our program
* player_performance.py: Our player performance program 
```
```
Annotated Bibliography

“Seaborn.Barplot.” Seaborn.Barplot - Seaborn 0.13.0 Documentation,
https://seaborn.pydata.org/generated/seaborn.barplot.html. Accessed 10 Dec. 2023.

Stumbling Through Data ScienceStumbling Through Data Science. “How to Display Custom
Values on a Bar Plot.” Stack Overflow, 4 Apr. 2017,
https://stackoverflow.com/questions/43214978/how-to-display-custom-values-on-a-bar-plot. Accessed 10 December 2023.
Before we learned about seaborn, I asked special permission from Aric to research how to create barplots and customize them for our project evaluation check in as at the time my only function at the time was a data visualization function. I used these websites to help me understand how to create a barplot, add titles to the x and y axis, and graph a dataframe.

Chung, Bryan Weather. “NBA Player Stats Dataset for the 2023-2024.” Kaggle, 11 Nov. 2023,
www.kaggle.com/datasets/bryanchungweather/nba-player-stats-dataset-for-the-2023-2024/data?select=NBA_2024_per_game%2813-11-2023%2BUpdated%29.csv. Accessed 10 December 2023.
This dataset provided us with extensive statistics for NBA players during the 2023–2024 regular season. The columns consist of the player's name, positions, team, assists, steals, blocks, etc. This CVS code is first opened, read through, and irritated through in order to read the stats of NBA players and teams. These stats are used throughout the entire code to compare players, show top teams, and to create a Pandas DataFrame

```