import numpy as np
from constants import NUM_TEAMS

def findRankInList(value, list):
    list.sort()
    return list.index(value)

def getPointsForThisCategory(this_team_val, all_teams_vals):
    return NUM_TEAMS - 1 - findRankInList(this_team_val, all_teams_vals)
