

# Hitters
class Player(): 

    def __init__(self, name, id, runs, rbi, homeruns, stolen_bases, batting_avg, strike_outs, positions_allowed):
        
        self.name = name
        self.id = id
        self.runs = runs 
        self.rbi = rbi
        self.homeruns = homeruns 
        self.stolen_bases = stolen_bases
        self.batting_avg = batting_avg
        self.strike_outs = strike_outs
        self.positions_allowed = positions_allowed
        self.position = "INIT"

    def disp(self): 
        print( "Name: ", self.name)
        print( "Runs: ", self.runs)
        print( "RBIs: ", self.rbi)
        print( "Homeruns: ", self.homeruns)
        print( "Stolen bases: ", self.stolen_bases)
        print( "Batting Avg: ", self.batting_avg)
        print( "Strike outs: ", self.strike_outs)
        print( "Position: ", self.position)
        print( "Positions allowed: ", self.positions_allowed)
        print()