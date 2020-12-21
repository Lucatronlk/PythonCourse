# Define a class for a football team, only the starting eleven (no substitutes/reserves)
# it can contain 3-5 defenders, 3-5 midfield players and 1-3 strikers; it has to have 11 players in total, 1 goalkeeper
# all players have stats from 1-10 (1 bad, 10 perfect)
# goalkeepers: communication, aerial reach, reflexes, passing, concentration, stamina, strength
# defenders: communication, tackling, heading, passing, concentration, stamina, strength
# midfield players: tackling, dribbling, heading, passing, concentration, stamina, strength
# strikers: dribbling, finishing, heading, passing, composure, stamina, strength
# create 3 teams of players, one with good players, one with medium players & one with weak players
from abc import ABC, abstractmethod
import random

class Player(ABC):
    @abstractmethod
    def __init__(self, passing, stamina, strength):

        self.passing = passing
        self.stamina = stamina
        self.strength = strength

class Defensive_Player(Player):
    @abstractmethod
    def __init__(self, communication, concentration, passing, stamina, strength):
        self.communication = communication
        self.concentration = concentration
        super().__init__(passing, stamina, strength)



# goalkeepers: communication, aerial reach, reflexes, passing, concentration, stamina, strength
class Goalkeeper(Defensive_Player):
    # the constructor
    def __init__(self, communication, passing, stamina, reflexes, aerial_reach, concentration, strength):
        #save value to object
        self.reflexes = reflexes
        self.aerial_reach = aerial_reach

        # call the parent constructor - Player
        super().__init__(communication, concentration, passing, stamina, strength)
        # call the parent constructor - DefensivePlayer
        #Defensive_Player.__init__(self, communication, concentration)


# defenders: communication, tackling, heading, passing, concentration, stamina, strength
class Defender(Defensive_Player):
    def __init__(self, communication, tackling, passing, concentration, stamina, heading, strength):

        self.tackling = tackling
        self.heading = heading


        #call the parent constructor - Player
        super().__init__(communication, concentration, passing, stamina, strength)
        # call the parent constructor - DefensivePlayer
        #Defensive_Player.__init__(self, communication, concentration)

# midfield players: tackling, dribbling, heading, passing, concentration, stamina, strength
class Midfielder(Player):
    def __init__(self, tackling, dribbling, passing, heading, concentration, stamina, strength ):
        self.dribbling = dribbling
        self.tackling = tackling
        self.heading = heading
        self.concentration = concentration

        #call the parent constructor - Player
        super().__init__(passing, stamina, strength)

class GoodMidfielder(Midfielder):
    def __init__(self):
        tackling, dribbling, passing, heading, concentration, stamina, strength = random.randint(7,10),random.randint(6,10), random.randint(9,10), random.randint(6,10), random.randint(9,10),random.randint(8,10), random.randint(9,10)
        super().__init__(tackling, dribbling, passing, heading, concentration, stamina, strength)


# strikers: dribbling, finishing, heading, passing, composure, stamina, strength
class Striker(Player):
    def __init__(self, dribbling, finishing, heading, composure, passing, stamina, strength ):
        self.dribbling = dribbling
        self.finishing = finishing
        self.heading = heading
        self.composure = composure

        #call the parent constructor
        super().__init__(passing, stamina, strength)



class Team:
    def __init__(self, goalkeepers, defenders, midfielders, strikers):
        self.goalkeepers = goalkeepers
        self.defenders = defenders
        self.midfielders = midfielders
        self.strikers = strikers

    def show(self):
        output = self.__dict__
        for player_type, list_players in output.items():
            print(player_type)
            for player in list_players:
                print(player.__dict__)


# gk1 = Goalkeeper(7,6,2,8,9,5,5)
# gk2 = Goalkeeper(8,7,3,9,10,6,6)
# gk3 = Goalkeeper(5,2,5,4,5,2,2)
# cb1 = Defender(6,7,2,8,7,8,9)
# cb2 = Defender(9,5,3,7,8,9,8)
# cm1 = Midfielder(10,1,8,2,7,6,8)
# cm2 = Midfielder(6,6,5,10,7,8,6)
st1 = Striker(10,9,6,8,5,8,8)
st2 = Striker(9,9,6,7,7,8,6)


i = 0
list_goalkeepers = []
while i < 3:
    x0, x1, x2, x3, x4, x5, x6 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    new_goalkeeper = Goalkeeper(x0, x1, x2, x3, x4, x5, x6)
    list_goalkeepers.append(new_goalkeeper)
    i+=1

i = 0
list_defenders = []
while i < 5:
  x0, x1, x2, x3, x4, x5, x6 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
  new_defender = Defender(x0, x1, x2, x3, x4, x4, x6)
  list_defenders.append(new_defender)
  i+=1

  # i = 0
  # list_midfielders = []
  # while i < 5:
  #     x0, x1, x2, x3, x4, x5, x6 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(
  #         1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
  #     new_midfielder = Midfielder(x0, x1, x2, x3, x4, x4, x6)
  #     list_midfielders.append(new_midfielder)
  #     i += 1
list_midfielders = 3 * [GoodMidfielder()]


team = Team(list_goalkeepers, list_defenders, list_midfielders, [st1, st2])

team.show()
#print(output)
# print(team.goalkeeper.__dict__)
# print(team.defenders[1].__dict__)
