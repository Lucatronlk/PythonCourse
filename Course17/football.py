# Define a class for a football team, only the starting eleven (no substitutes/reserves)
# it can contain 3-5 defenders, 3-5 midfield players and 1-3 strikers; it has to have 11 players in total, 1 goalkeeper
# all players have stats from 1-10 (1 bad, 10 perfect)
# goalkeepers: communication, aerial reach, reflexes, passing, concentration, stamina, strength
# defenders: communication, tackling, heading, passing, concentration, stamina, strength
# midfield players: tackling, dribbling, heading, passing, concentration, stamina, strength
# strikers: dribbling, finishing, heading, passing, composure, stamina, strength
# create 3 teams of players, one with good players, one with medium players & one with weak players


class Player:
    def __init__(self, passing, stamina):

        self.passing = passing
        self.stamina = stamina


class Goalkeeper(Player):
    def __init__(self, communication, passing, stamina, reflexes):
        #save value to object
        self.reflexes = reflexes
        self.communication = communication
        super().__init__(passing, stamina)


class Defender(Player):
    def __init__(self, communication, tackling, passing, stamina):

        self.tackling = tackling
        self.communication = communication
        #call the parent constructor
        super().__init__(passing, stamina)


class Midfielder(Player):

    def __init__(self, tackling, dribbling, passing, stamina ):
        self.dribbling = dribbling
        self.tackling = tackling
        #call the parent constructor
        super().__init__(passing, stamina)

class Striker(Player):
    def __init__(self, dribbling, finishing, passing, stamina ):
        self.dribbling = dribbling
        self.finishing = finishing
        #call the parent constructor
        super().__init__(passing, stamina)



class Team:
    def __init__(self, goalkeeper, defenders, midfielders, strikers):
        self.goalkeeper = goalkeeper
        self.defenders = defenders
        self.midfielders = midfielders
        self.strikers = strikers

gk1 = Goalkeeper(8,5,3,2)
cb1 = Defender(6, 7, 2, 8)
cb2 = Defender(9, 5, 3, 7)
cm1 = Midfielder(10, 1, 8, 2)
cm2 = Midfielder(6, 6, 5, 10)
st1 = Striker(10, 9, 6, 8)
st2 = Striker(9, 9, 6, 7)
team = Team(gk1, [cb1, cb2], [cm1, cm2], [st1, st2])
