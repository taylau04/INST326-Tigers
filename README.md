# INST326-Tigers

Example Runs:

```
% python3 collaborative_programming.py -h                                                 
usage: collaborative_programming.py [-h] file action

positional arguments:
  file        Path to the file containing player statistics
  action      Name of the action to run: compare_players | show_best_teams | player_stats_by_team

options:
  -h, --help  show this help message and exit

```

```
% python3 collaborative_programming.py NBA_2024_per_game\(28-11-2023\).csv compare_players     
Enter Player 1's name: Lebron James
Player 1 Grade: B, Numeric Score: 84.98
Enter Player 2's name: Grayson Allen
Player 2 Grade: F, Numeric Score: 41.040000000000006
Lebron James received a higher performance score than Grayson Allen
```

```
% python3 collaborative_programming.py NBA_2024_per_game\(28-11-2023\).csv show_best_teams     
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
% python3 collaborative_programming.py NBA_2024_per_game\(28-11-2023\).csv player_stats_by_team
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