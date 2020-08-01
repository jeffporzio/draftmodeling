from constants import NUM_TEAMS
import numpy as np

class LeagueRankData(): 

    def __init__(self, stats): 

        self.runs_ranks = []
        self.rbi_ranks = []
        self.homeruns_ranks = []
        self.stolen_bases_ranks = []
        self.batting_avg_ranks = []
        self.strike_outs_ranks = []

        self.runs_ranks_std = []
        self.rbi_ranks_std = []
        self.homeruns_ranks_std = []
        self.stolen_bases_ranks_std = []
        self.batting_avg_ranks_std = []
        self.strike_outs_ranks_std = []

        for i in range(0,NUM_TEAMS):
            self.runs_ranks.append(int(np.mean([stat.runs[i] for stat in stats])))
            self.runs_ranks_std.append(int(np.std([stat.runs[i] for stat in stats])))

            self.rbi_ranks.append(int(np.mean([stat.rbi[i] for stat in stats])))
            self.rbi_ranks_std.append(int(np.std([stat.rbi[i] for stat in stats])))

            self.homeruns_ranks.append(int(np.mean([stat.homeruns[i] for stat in stats])))
            self.homeruns_ranks_std.append(int(np.std([stat.homeruns[i] for stat in stats])))

            self.stolen_bases_ranks.append(int(np.mean([stat.stolen_bases[i] for stat in stats])))
            self.stolen_bases_ranks_std.append(int(np.std([stat.stolen_bases[i] for stat in stats])))

            self.batting_avg_ranks.append(int(np.mean([stat.batting_avg[i]*1000 for stat in stats]))/float(1000))
            self.batting_avg_ranks_std.append(int(np.std([stat.batting_avg[i]*1000 for stat in stats]))/float(1000))

            self.strike_outs_ranks.append(int(np.mean([stat.strike_outs[i] for stat in stats])))
            self.strike_outs_ranks_std.append(int(np.std([stat.strike_outs[i] for stat in stats])))

    def disp(self):
        print "Avg runs by rank: ", zip( self.runs_ranks, self.runs_ranks_std)
        print "Avg rbi by rank: ", zip( self.rbi_ranks, self.rbi_ranks_std )
        print "Avg homeruns by rank: ", zip( self.homeruns_ranks, self.homeruns_ranks_std )
        print "Avg stolen bases by rank: ", zip( self.stolen_bases_ranks, self.stolen_bases_ranks_std )
        print "Avg batting avg by rank: ", zip( self.batting_avg_ranks, self.batting_avg_ranks_std )
        print "Avg stike outs by rank: ", zip( self.strike_outs_ranks, self.strike_outs_ranks_std )

