from team import Team
from playerpool import Playerpool
from constants import NUM_TEAMS
import numpy as np
from leagueStats import LeagueStats
from functools import reduce
from util.log import *

class League(object):

    def __init__(self):
        logging.info("Initializing league...")
        self.player_pool = Playerpool()
        
        self.teams = []
        self.final_teams = []

        for i in range(0,NUM_TEAMS):
            name = "Team " + str(i)
            team = Team(name)
            self.teams.append(team)
            logging.info("Created team: " + name)
        
        logging.info("Finished creating league.")

    def doDraft(self):
        logging.info("Performing draft...")
        for player in self.player_pool.pool:

            # Check if the teams are full:
            all_teams_are_full = reduce(
                lambda x, y: x and y, 
                [x.isFull() for x in self.teams], 
                True
            )
            if all_teams_are_full:
                logging.info("Finished draft, all teams are full.")
                break

            # Rather than have teams bid round by round, just ask how much each would bid and beat the bid by $1
            bids = [ team.predict_player_value(player) for team in self.teams ]
            highest_bid = max(bids)

            try:
                second_highest_bid = max( list( filter(lambda x: (x < highest_bid), bids) ) )
            except ValueError:
                logging.debug("Error in bidding: ", list( filter(lambda x: (x < highest_bid), bids) ))
                second_highest_bid = 0

            winning_bid = highest_bid
            if winning_bid > second_highest_bid: 
                winning_bid = second_highest_bid + 1

            winning_team_index = bids.index(highest_bid)
            highest_bidder = self.teams[winning_team_index]
            highest_bidder.purchase_player(player, winning_bid)

            if highest_bidder.isFull():
                self.final_teams.append(self.teams.pop(winning_team_index))

    def disp(self):
        for team in self.final_teams:
            team.disp()

def main():
    logging.info("Starting in main...")
    league = League()
    league.doDraft()

    leagueStats = LeagueStats(league)
    leagueStats.disp()

    logging.info("Finished in mains.")



if __name__ == "__main__":
    main()