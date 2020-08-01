
from constants import *
from player import Player

# Place holder: 
from random import randrange, seed

seed(randrange(1000000000))

empty_pos_dict = {}
for position in POSITIONS:
    empty_pos_dict[position] = 0


class Team(): 
    def __init__(self, name):
        
        self.player_list = []
        self.position_dict = {}
        self.money = MONEY
        

        self.name = name
        self.runs = 0 
        self.rbi = 0
        self.homeruns = 0
        self.stolen_bases = 0
        self.batting_avg = 0
        self.strike_outs = 0


    def purchase_player(self, player, cost): 
        self.player_list.append(player)
        self.money -= cost

        self.update_position_dict()
        self.update_team_stats()

    def update_position_dict(self):
        self.position_dict = empty_pos_dict
        # To do

    def update_team_stats(self):
        self.runs         = sum( x.runs         for x in self.player_list)
        self.rbi          = sum( x.rbi          for x in self.player_list)
        self.homeruns     = sum( x.homeruns     for x in self.player_list)
        self.stolen_bases = sum( x.stolen_bases for x in self.player_list)
        self.batting_avg  = sum( x.batting_avg  for x in self.player_list)/len(self.player_list)
        self.strike_outs  = sum( x.strike_outs  for x in self.player_list)


    def find_optimal_positions(self):
        pass 

    def predict_player_value(self, player):

        # bid negative if full
        if self.isFull():
            return -1

        value = randrange(0,60)
        # Stop the team from spending too much
        roster_size = len(self.player_list)
        max_bid_allowed = self.money - (NUM_PLAYERS_PER_TEAM - roster_size) + 1

        if value < max_bid_allowed: 
            return value 
        else: 
            return max_bid_allowed 


    def isFull(self): 
        if len(self.player_list) >= NUM_PLAYERS_PER_TEAM:
            return True
        else: 
            return False


    def disp(self):
        print
        print "*** Roster: *** "
        print "Size: ", len(self.player_list)
        for player in self.player_list: 
            print player.name

        print "Runs: ", self.runs
        print "RBI: ", self.rbi
        print "Homeruns: ", self.homeruns
        print "Stolen bases:", self.stolen_bases
        print "Batting AVG: ", self.batting_avg
        print "Stike outs: ", self.strike_outs

        print "Remaining Money: ", self.money
        
        print