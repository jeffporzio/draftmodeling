from team import Team
from playerpool import Playerpool
from constants import NUM_TEAMS
import numpy as np
from leagueStats import LeagueStats
from functools import reduce


class League():

    def __init__(self):
        self.player_pool = Playerpool()
        
        self.teams = []
        self.final_teams = []

        for i in range(0,NUM_TEAMS):
            name = "Team " + str(i)
            team = Team(name)
            self.teams.append(team)

    def doDraft(self):
        for player in self.player_pool.pool:

            # Check if the teams are full:
            all_teams_are_full = reduce(lambda x, y: x and y, [x.isFull() for x in self.teams], True)
            if all_teams_are_full:
                break

            bids = [ x.predict_player_value(player) for x in self.teams ]
            highest_bid = max(bids)

            winning_team_index = bids.index(highest_bid)
            highest_bidder = self.teams[winning_team_index]
            highest_bidder.purchase_player(player, highest_bid)

            if highest_bidder.isFull():
                self.final_teams.append(self.teams.pop(winning_team_index))



    def playSeason(self):
        pass


    def disp(self):
        for team in self.final_teams:
            team.disp()

def main():
    league = League()
    league.doDraft()

    leagueStats = LeagueStats(league)
    leagueStats.disp()




if __name__ == "__main__":
    main()