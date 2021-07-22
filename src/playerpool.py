from player import Player
import os
from random import shuffle
from util.log import *
from getSeasonData import getSeasonalBatterData, getSeasonalPitcherData

# Placeholder
from constants import POSITIONS

class Playerpool(object): 

    def __init__(self):
        self.pool = self.createPool()
        shuffle(self.pool)

    def createPool(self):
        logging.info("Initializing PlayerPool...")
        pool = []
        batter_df = getSeasonalBatterData("2019") 
        for batter in batter_df.iterrows():
            playerData = batter[1]
            name = playerData.Name
            id = playerData.mlb_ID
            runs = playerData.R
            rbi = playerData.RBI
            homeruns = playerData.HR
            stolen_bases = playerData.SB
            batting_avg = playerData.BA
            strike_outs = playerData.SO
            positions_allowed = POSITIONS # TODO: What?

            batter = Player(name, id, runs, rbi, homeruns, stolen_bases, batting_avg, strike_outs, positions_allowed)
            pool.append(batter)

        pitcher_df = getSeasonalPitcherData("2019")
        print(pitcher_df.columns)
        # for pitcher in pitcher_df.iterrows(): 
        

        logging.info("Finished creating PlayerPool")
        return pool

    def disp(self):
        for player in self.pool: 
            player.disp()

def main():
    pool = Playerpool()
    pool.disp()

if __name__ == "__main__":
    main()
