from dailydraft.player import Batter, BatterStats, BatterStatsBuilder, Pitcher, PitcherStats, PitcherStatsBuilder
from typing import List
import os
from random import shuffle
from dailydraft.util.log import *
from dailydraft.getPlayerData import getDailyPitcherData, getDailyBatterData #, getSeasonalBatterData, getSeasonalPitcherData

# Placeholder
from dailydraft.util.constants import Positions

class Playerpool(object): 

    def __init__(self, date):
        self.batterPool: List(Batter) = [] 
        self.pitcherPool: List(Pitcher) = [] 
        self.createPool(date)
        shuffle(self.batterPool)
        shuffle(self.pitcherPool)

    def createPool(self, date):
        logging.info("Initializing PlayerPool...")
        batter_df = getDailyBatterData(date) 
        pitcher_df = getDailyPitcherData(date)

        # print(batter_df.columns)
        # print(pitcher_df.columns)

        # TODO: Figure out how to get player position
        for batterData in batter_df.iterrows():
            playerData = batterData[1]
            batterStatsBuilder: BatterStatsBuilder = BatterStatsBuilder()
            batterStats: BatterStats = batterStatsBuilder \
                .setHits(playerData.H) \
                .setDoubles(playerData['2B']) \
                .setTriples(playerData['3B']) \
                .setHomeruns(playerData.HR) \
                .setRunsBattedIn(playerData.RBI) \
                .setRuns(playerData.R) \
                .setBaseOnBalls(playerData.BB + playerData.IBB) \
                .setHitByPitch(playerData.HBP) \
                .setSacrificeFlies(playerData.SF) \
                .setSacrificeHits(playerData.SH) \
                .setStolenBases(playerData.SB) \
                .build() 
            name = playerData.Name
            id = playerData.mlb_ID
            batter: Batter = Batter(name, id, batterStats, Positions.INIT)
            self.batterPool.append(batter)

        # TODO: Figure out how to tell if starter 
        # TODO: Figure out how to tell if they won (double header for releif pitcher?)
        for pitcherData in pitcher_df.iterrows(): 
            playerData = pitcherData[1]
            pitcherStatsBuilder: PitcherStatsBuilder = PitcherStatsBuilder()
            pitcherStats: PitcherStats = pitcherStatsBuilder \
                .setIsStartingPitcher(-1) \
                .setInningsPitched(playerData.IP) \
                .setStrikeouts(playerData.SO) \
                .setDidWin(-1) \
                .setEarnedRunAllowed(playerData.ER) \
                .setHitsAgainst(playerData.H) \
                .setBaseOnBallsAgainst(playerData.BB + playerData.IBB) \
                .setHitsBatsman(playerData.HBP) \
                .setHolds(-1) \
                .setSaves(playerData.SV) \
                .setDidCompleteGame(playerData.IP >= 9) \
                .build()
            name = playerData.Name
            id = -1 # playerData.mlb_ID
            pitcher: Pitcher = Pitcher(name, id, pitcherStats, Positions.PITCHER)
            self.pitcherPool.append(pitcher)

        # Actually put the data in the containers

        logging.info("Finished creating PlayerPool")

    def disp(self):
        for batter in self.batterPool: 
            print(batter)
        for pitcher in self.pitcherPool: 
            print(pitcher)


if __name__ == "__main__":
    pool = Playerpool()
    pool.disp()
