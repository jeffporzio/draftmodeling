from player import Player
import os
import csv
from math import ceil
from random import shuffle

# Placeholder
from constants import POSITIONS

class Playerpool(): 

    def __init__(self):
        self.pool = self.createPool()
        shuffle(self.pool)

    def createPool(self):
        
        pool = []
        
        dir = "data/"
        files = os.listdir(dir)
        
        for file in files:
            if file != "data_2019.csv":
                continue

            with open(dir+file, "r") as f: 
                reader = csv.reader(f)
                next(reader) # Skip header line
                for row in reader: 
                    name = row[0]
                    id = int(row[21])
                    runs = int(row[5])
                    rbi = int(row[6])
                    homeruns = int(row[4])
                    stolen_bases = int(row[7])
                    batting_avg = float(row[12])
                    strike_outs = int(ceil(float(row[3]) * float(row[9][:-1])/100)) # Help?
                    positions_allowed = POSITIONS # row[1] # Didn't get this?

                    player = Player(name, id, runs, rbi, homeruns, stolen_bases, batting_avg, strike_outs, positions_allowed)
                    pool.append(player)

        return pool

    def disp(self):
        for player in self.pool: 
            player.disp()

def main():
    pool = Playerpool()
    pool.disp()

if __name__ == "__main__":
    main()
