from util.log import *
from league import League
import numpy as np
from util.calculations import getPointsForThisCategory

class Season(object): 

    def __init__(self):

        # Creat league and do a draft
        league = League()
        league.doDraft()
        self.teams = league.final_teams
        
        # Initialize points with zeros
        self.teamScores = {}
        for team in self.teams: 
            self.teamScores[team.name] = 0

    def playSeason(self):

        for team in self.teams: 
            runs_points = getPointsForThisCategory(team.runs, [team.runs for team in self.teams])
            rbi_points = getPointsForThisCategory(team.rbi, [team.rbi for team in self.teams]) 
            home_run_points = getPointsForThisCategory(team.homeruns, [team.homeruns for team in self.teams])
            stolen_bases_points = getPointsForThisCategory(team.stolen_bases, [team.stolen_bases for team in self.teams])
            batting_avg_points = getPointsForThisCategory(team.batting_avg, [team.batting_avg for team in self.teams])
            strike_outs_points = getPointsForThisCategory(team.strike_outs, [team.strike_outs for team in self.teams])
            
            points = runs_points + rbi_points + home_run_points + stolen_bases_points + batting_avg_points + strike_outs_points
            self.teamScores[team.name] = points


def main():
    logging.info("Starting season...")

    season = Season()
    season.playSeason()
    print( season.teamScores )

    logging.info("Finished season.")

if __name__ == "__main__":
    main()