from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams

date = '2021-02-16'


# Get **all** the games so we can filter to an individual GAME_ID
result = leaguegamefinder.LeagueGameFinder()
all_games = result.get_data_frames()[0]
# Find the game_id we want

# Get all Teams shortcuts
team_list = teams.get_teams()
team_abbr = []
for team in team_list:
    abbriviation = team["abbreviation"]
    team_abbr.append(abbriviation)

# Search for correct games and teams

# working
full_game = all_games[all_games.GAME_DATE == date]

# not working
full_game_test = all_games[all_games.GAME_DATE == date & all_games.TEAM_ABBREVIATION in team_abbr]


#print(full_game)

print(type(full_game))
# 6,9,27

scoreboard = full_game[['MATCHUP','WL', 'PTS','PLUS_MINUS']]