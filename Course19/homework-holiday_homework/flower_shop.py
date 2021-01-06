# Create a flower shop application which deals in flower objects 
# and use those flower objects in a bouquet object which can then be sold. 
# Keep track of the number of objects and when you may need to order more (keep them in a file) 
# Allow the user to give commands through the terminal (use sys.argv to read the commands)
# Make unit tests

import sys
import abc

class Flower(abc.ABC):

    @abc.abstractmethod

    def __init__(self, colour, smell, petals):
        self.colour = colour
        self.smell = smell
        self.petals = petals


    # def __init__(self, rose, tulip, lily, orchid):
    #     self.rose = rose
    #     self.tulip = tulip
    #     self.lily = lily
    #     self.orchid = orchid


class Rose(Flower):

    def __init__(self, colour,  petals):

        super().__init__(colour, 'relaxing', petals)


class Tulip(Flower):

    def __init__(self, colour, petals):
        super().__init__(colour, 'honey', petals)


class Orchid(Flower):
    def __init__(self, colour, petals):
        super().__init__(colour, 'cinnamon', petals)

class Bouquet:
    def __init__(self, flowers):

        self.flowers = flowers

    def get_smell(self):
         smells = {}
         for one_flower in self.flowers:
             smells[one_flower.smell] = smells[one_flower.smell] + 1 if one_flower.smell in smells else 1
             # if one_flower.smell in smells:
             #   smells[one_flower.smell] += 1
             # else:
             #     smells[one_flower.smell] = 1
         return smells




class FlowerShop:
    def place_order(self, flowers):
        bouquet = Bouquet(flowers)
        return bouquet


shop = FlowerShop()
order = shop.place_order([Tulip('red', 6), Orchid('white', 3), Orchid('white', 4)])
print(order.get_smell())



