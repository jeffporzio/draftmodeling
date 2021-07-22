from enum import Enum

# TODO: Are these different for daily?
class Positions(Enum):
    PITCHER = "PITCHER"
    CATCHER = "CATCHER"
    FIRST_BASE = "FIRST_BASE" 
    SECOND_BASE = "SECOND_BASE"
    SHORTSTOP = "SHORTSTOP"
    THIRD_BASE = "THIRD_BASE"
    OUTFIELD = "OUTFIELD"
    UTIL = "UTIL"
    BENCH = "BENCH"
    INIT = "INIT"

POSITION_REQS = {"CATCHER":1,
                "FIRST_BASE":1,
                "SECOND_BASE":1,
                "SHORTSTOP":1,
                "THIRD_BASE":1,
                "OUTFIELD":3,
                "UTIL":1,
                "BENCH":0
                }

NUM_PLAYERS_PER_TEAM = 12

MONEY = 170 # 260

NUM_TEAMS = 11


SEASON_START_MONTH_DAY = '03-15'
SEASON_END_MONTH_DAY = '10-15'


"""
Scoring Notes
- Hitting statistics for Pitchers will not be counted, and Pitching statistics for Hitters will not be counted.
- Pitchers will be scored based on their listed position on DraftKings. I.e. a pitcher who is listed as a starting pitcher (SP) on DraftKings will be scored as a starting pitcher even if he does not end up starting the game.
- Holds will be scored using MLB's official definition of a Hold.
"""
class  dailyHitterPoints(Enum): 
    SINGLE = 3
    DOUBLE = 5
    TRIPLE = 8 
    HOMERUN = 10
    RUN_BATTED_IN = 2
    RUN = 2
    BASE_ON_BALLS = 2
    HIT_BY_PITCH = 2
    SACRIFICE_FLY = 1.25
    SACRIFICE_HIT = 1.25
    STOLEN_BASE = 5

class dailyPitcherPoints(Enum):
    INNING_PITCHED_SP = 2.25
    INNING_PITCHED_RP = 3.9 
    STRIKEOUT_SP = 2
    STRIKEOUT_RP = 3    
    WIN = 4
    EARNED_RUN_ALLOWED = -2
    HIT_AGGAINST = -0.6
    BASE_ON_BALLS_AGAINST = -0.6 
    HIT_BATSMAN = -0.6
    HOLD = 2.5
    SAVE = 5
    COMPLETE_GAME = 2.5 
    COMPLETE_GAME_SHUTOUT = 2.5
    NO_HITTER = 5
    TEN_OR_MORE_STRIKEOUTS = 2
    SEVEN_OR_MORE_INNINGS_PITCHED = 1.25