import sys
sys.path.append('C:\\Users\\jeffp\\repos\\draftmodeling\\flaskDraft\\dailydraft') 

from player import Batter
from util.log import logging
from baseball_scraper import batting_stats_range, pitching_stats_range
# from util.constants import SEASON_START_MONTH_DAY, SEASON_END_MONTH_DAY

# def getSeasonalBatterData(seasonYear):
#     seasonStartDate = seasonYear+"-"+SEASON_START_MONTH_DAY
#     seasonEndData = seasonYear+"-"+SEASON_END_MONTH_DAY
#     logging.info("Fetching batter info for Season: "+seasonYear)
#     df = batting_stats_range(seasonStartDate, seasonEndData)
#     return df

# def getSeasonalPitcherData(seasonYear): 
#     seasonStartDate = seasonYear+"-"+SEASON_START_MONTH_DAY
#     seasonEndData = seasonYear+"-"+SEASON_END_MONTH_DAY
#     logging.info("Fetching pitcher info for Season: "+seasonYear)
#     df = pitching_stats_range(seasonStartDate, seasonEndData)
#     return df

def getDailyBatterData(date): 
    logging.info(f"Fetching Batter data for: {date}")
    df = batting_stats_range(date,)
    return df

def getDailyPitcherData(date):
    logging.info(f"Fetching Pitcher data for {date}")
    df = pitching_stats_range(date,)
    return df

def main(): 
    batter_df = getDailyBatterData("2021-07-21")
    print( batter_df )

if __name__ == "__main__": 
    main()