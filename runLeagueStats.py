from league import League
from leagueStats import LeagueStats
import numpy as np
from constants import NUM_TEAMS
from leagueRankData import LeagueRankData

N = int(5000)

def main(): 
    
    stats = []
    print "Starting MC Simulation..."
    for i in range(0,N):

        if i % 1000 == 0 and i > 0: 
            print "Compeleted %i of %i iterations" % (i, N)

        league = League()
        league.doDraft()

        leagueStats = LeagueStats(league)

        stats.append(leagueStats)
    print "Finished MC Simulation."

    aggregateStats(stats)
    

def aggregateStats(stats):
    runs_avg = [x.runs_avg for x in stats]
    rbi_avg = [x.rbi_avg for x in stats]
    homeruns_avg = [x.homeruns_avg for x in stats]
    stolen_bases_avg = [x.stolen_bases_avg for x in stats]
    batting_avg_avg = [x.batting_avg_avg for x in stats]
    strike_outs_avg = [x.strike_outs_avg for x in stats]

    runs_std = [x.runs_std for x in stats]
    rbi_std = [x.rbi_std for x in stats]
    homeruns_std = [x.homeruns_std for x in stats]
    stolen_bases_std = [x.stolen_bases_std for x in stats]
    batting_avg_std = [x.batting_avg_std for x in stats]
    strike_outs_std = [x.strike_outs_std for x in stats]

    leagueRanks = LeagueRankData(stats)
    leagueRanks.disp()






if __name__ == "__main__":
    main()