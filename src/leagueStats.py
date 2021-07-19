import numpy as np

class LeagueStats():

    def __init__(self, league):

        teams = league.final_teams

        self.runs = [x.runs for x in teams]
        self.rbi = [x.rbi for x in teams]
        self.homeruns = [x.homeruns for x in teams]
        self.stolen_bases = [x.stolen_bases for x in teams]
        self.batting_avg = [x.batting_avg for x in teams]
        self.strike_outs = [x.strike_outs for x in teams]

        self.runs_avg = np.mean(self.runs)
        self.rbi_avg = np.mean(self.rbi)
        self.homeruns_avg = np.mean(self.homeruns)
        self.stolen_bases_avg = np.mean(self.stolen_bases)
        self.batting_avg_avg = np.mean(self.batting_avg)
        self.strike_outs_avg = np.mean(self.strike_outs)

        self.runs_std = np.std(self.runs) 
        self.rbi_std = np.std(self.rbi)
        self.homeruns_std = np.std(self.homeruns)
        self.stolen_bases_std = np.std(self.stolen_bases)
        self.batting_avg_std = np.std(self.batting_avg)
        self.strike_outs_std = np.std(self.strike_outs)

        self.runs.sort(reverse=True)
        self.rbi.sort(reverse=True)
        self.homeruns.sort(reverse=True)
        self.stolen_bases.sort(reverse=True)
        self.batting_avg.sort(reverse=True)
        self.strike_outs.sort(reverse=True)

    def disp(self): 
        print( "Runs: %f +/- %f" % (self.runs_avg, self.runs_std))
        print( "RBI: %f +/- %f" % (self.rbi_avg, self.rbi_std))
        print( "HRs: %f +/- %f" % (self.homeruns_avg, self.homeruns_std))
        print( "SBs: %f +/- %f" % (self.stolen_bases_avg, self.stolen_bases_std))
        print( "AVG: %f +/- %f" % (self.batting_avg_avg, self.batting_avg_std))
        print( "SOs: %f +/- %f" % (self.strike_outs_avg, self.strike_outs_std))

