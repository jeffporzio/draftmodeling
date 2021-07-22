from util.log import logging
from baseball_scraper import batting_stats_range, pitching_stats_range
from constants import SEASON_START_MONTH_DAY, SEASON_END_MONTH_DAY

def getSeasonalBatterData(seasonYear):
    seasonStartDate = seasonYear+"-"+SEASON_START_MONTH_DAY
    seasonEndData = seasonYear+"-"+SEASON_END_MONTH_DAY
    logging.info("Fetching batter info for Season: "+seasonYear)
    df = batting_stats_range(seasonStartDate, seasonEndData)
    return df

def getSeasonalPitcherData(seasonYear): 
    seasonStartDate = seasonYear+"-"+SEASON_START_MONTH_DAY
    seasonEndData = seasonYear+"-"+SEASON_END_MONTH_DAY
    logging.info("Fetching pitcher info for Season: "+seasonYear)
    df = pitching_stats_range(seasonStartDate, seasonEndData)
    return df

def main(): 
    getSeasonalBatterData("2019")