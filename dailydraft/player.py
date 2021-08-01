from abc import ABC
from typing import Union

from constants import Positions

class Stats(ABC):
    def __repr__(self): 
        output: str = ""
        temp = vars(self)
        for item in temp:
            output += f"{item}  :  {temp[item]}\n\t"
        return output[:-2]

class BatterStats(Stats): 
    def __init__(self):
        self.hits: int
        self.singles: int
        self.doubles: int
        self.triples: int
        self.homeruns: int
        self.ruslBattedIn: int
        self.runs : int
        self.baseOnBalls: int 
        self.hitByPitch: int
        self.sacrificeFlies: int
        self.sacrificeHits: int
        self.stolenBases: int


class BatterStatsBuilder(object): 
    def __init__(self): 
        self.batterStats: BatterStats = BatterStats()

    def build(self)  -> BatterStats:
        self.batterStats.singles = self.batterStats.hits - self.batterStats.homeruns - self.batterStats.doubles
        return self.batterStats

    def setHits(self, input):
        self.batterStats.hits = input
        return self

    def setDoubles(self, input):
        self.batterStats.doubles = input
        return self

    def setTriples(self, input):
        self.batterStats.triples = input
        return self

    def setHomeruns(self, input):
        self.batterStats.homeruns = input
        return self

    def setRunsBattedIn(self, input):
        self.batterStats.runsBattedIn = input
        return self

    def setRuns(self, input):
        self.batterStats.runs = input
        return self

    def setBaseOnBalls(self, input):
        self.batterStats.baseOnBalls = input
        return self

    def setHitByPitch(self, input):
        self.batterStats.hitByPitch = input
        return self

    def setSacrificeFlies(self, input):
        self.batterStats.sacrificeFlies = input
        return self

    def setSacrificeHits(self, input):
        self.batterStats.sacrificeHits = input
        return self

    def setStolenBases(self, input):
        self.batterStats.stolenBases = input
        return self


class PitcherStats(Stats):
    def __init__(self):
        self.isStartingPitcher: bool
        self.inningsPitched: int
        self.strikeouts: int
        self.didWin: bool
        self.earnedRunAllowed: int
        self.hitsAgainst: int
        self.baseOnBallsAgainst: int 
        self.hitsBatsman: int
        self.holds: int
        self.saves: int
        self.didCompleteGame: bool
        self.didNoHitter: bool
        self.didCompleteGameShutout:  bool
        self.didTenOrMoreStrikeOuts: bool
        self.didSevenOrMoreInningsPitched: bool

class PitcherStatsBuilder: 
    def __init__(self):
        self.pitcherStats: PitcherStats = PitcherStats()

    def setIsStartingPitcher(self, input):
        self.pitcherStats.isStartingPitcher = input
        return self

    def setInningsPitched(self, input):
        self.pitcherStats.inningsPitched = input
        return self

    def setStrikeouts(self, input):
        self.pitcherStats.strikeouts = input
        return self

    def setDidWin(self, input):
        self.pitcherStats.didWin = input
        return self

    def setEarnedRunAllowed(self, input):
        self.pitcherStats.earnedRunAllowed = input
        return self

    def setHitsAgainst(self, input):
        self.pitcherStats.hitsAgainst = input
        return self

    def setBaseOnBallsAgainst(self, input):
        self.pitcherStats.baseOnBallsAgainst = input
        return self

    def setHitsBatsman(self, input):
        self.pitcherStats.hitsBatsman = input
        return self

    def setHolds(self, input):
        self.pitcherStats.holds = input
        return self

    def setSaves(self, input):
        self.pitcherStats.saves = input
        return self

    def setDidCompleteGame(self, input):
        self.pitcherStats.didCompleteGame = input
        return self

    def build(self) -> PitcherStats: 
        self.pitcherStats.didNoHitter = self.pitcherStats.hitsAgainst == 0
        self.pitcherStats.didCompleteGameShutout = self.pitcherStats.inningsPitched >= 9 and self.pitcherStats.earnedRunAllowed == 0
        self.pitcherStats.didSevenOrMoreInningsPitched = self.pitcherStats.inningsPitched >= 7
        self.pitcherStats.didTenOrMoreStrikeOuts = self.pitcherStats.strikeouts >= 10
        return self.pitcherStats


class Player(object):

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.stats: Union[BatterStats, PitcherStats]
        self.position: str = Positions.INIT

    def __repr__(self): 
        return f"""
        Name: {self.name}
        Id: {self.id}
        {repr( self.stats )}
        Position: {self.position}
        """
class Batter(Player):
    def __init__(self, name: str, id: int, batterStats: BatterStats, position: str):
        Player.__init__(self, name, id)
        self.stats = batterStats
        self.position = position


class Pitcher(Player):
    def __init__(self, name: str, id: int, pitcherStats: PitcherStats, position: str):
        Player.__init__(self, name, id)
        self.stats = pitcherStats
        self.position = position




if __name__ == "__main__":
    batterStatsBuilder: BatterStatsBuilder = BatterStatsBuilder()
    batterStats: BatterStats = batterStatsBuilder \
        .setHits(1) \
        .setDoubles(2) \
        .setTriples(3) \
        .setHomeruns(4) \
        .setRunsBattedIn(5) \
        .setRuns(6) \
        .setBaseOnBalls(7) \
        .setHitByPitch(8) \
        .setSacrificeFlies(9) \
        .setSacrificeHits(10) \
        .setStolenBases(11) \
        .build() 

    pitcherStatsBuilder: PitcherStatsBuilder = PitcherStatsBuilder()
    pitcherStats: PitcherStats = pitcherStatsBuilder \
        .setIsStartingPitcher(1) \
        .setInningsPitched(2) \
        .setStrikeouts(3) \
        .setDidWin(4) \
        .setEarnedRunAllowed(5) \
        .setHitsAgainst(6) \
        .setBaseOnBallsAgainst(7) \
        .setHitsBatsman(8) \
        .setHolds(9) \
        .setSaves(10) \
        .setDidCompleteGame(11) \
        .build()

    
    batter: Batter = Batter("John Smith", 1, batterStats, Positions.OUTFIELD)
    print(batter)

    pitcher: Pitcher = Pitcher("Jane Doe", 2, pitcherStats, Positions.PITCHER)
    print(pitcher)