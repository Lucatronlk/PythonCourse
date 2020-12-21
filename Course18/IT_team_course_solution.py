from skill import SalesSkill, ManagingSkill


class Name:
    #constructor
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def show(self):
        print('First name: ' + self.first)
        print('Last name ' + self.last)



class SalesPerson:
    def __init__(self, name, number_of_sales, skill):

        self.name = name
        self.number_of_sales = number_of_sales
        self.skill = skill

    def show(self):
        self.name.show()
        print('Number of sales ' + str(self.number_of_sales))
        self.skill.show()


class ProductOwner:
    def __init__(self, name, managed_teams, skill):
        self.name = name
        self.managed_teams = managed_teams
        self.skill = skill

    def show(self):
        self.name.show()
        print('Managed Teams: ' + str(self.managed_teams))
        self.skill.show()


# davide = SalesPerson(Name('Davide', 'Ravasi'), 100, SalesSkill(10))
# mircea = ProductOwner(Name('Mircea', 'Pop'), ['os-backend', 'os-frontend'], ManagingSkill(9))
#
# davide.show()
# mircea.show()