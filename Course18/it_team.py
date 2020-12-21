import random


class Name:
    def __init__(self, first_name, last_name):

        self.first_name = first_name
        self.last_name = last_name



class SalesPersons(Name):
    def __init__(self, first_name, last_name, number_of_sales, sales_talent):

        self.number_of_sales = number_of_sales
        self.sales_talent = sales_talent
        super().__init__(first_name,last_name)

class ShareHolders(Name):

    def __init__(self,first_name, last_name, percentage_of_shares):
      self.percentage_of_shares = percentage_of_shares

      super().__init__(first_name, last_name)


class Devs(Name):

       def __init__(self, first_name, last_name, years_of_experience, backend_skill, frontend_skill, devops_skill, system_knowledge, testing_skill, designer_skill):

         self.years_of_experience = years_of_experience
         self.backend_skill = backend_skill
         self.frontend_skill = frontend_skill
         self.devops_skill = devops_skill
         self.system_knowledge = system_knowledge
         self.testing_skill = testing_skill
         self.designer_skill = designer_skill

         super().__init__(first_name, last_name)

class ProductOwners(Name):
    def __init__(self, first_name, last_name, managed_teams, managing_talent):
        self.managed_teams = managed_teams
        self.managing_talent = managing_talent

        super().__init__(first_name, last_name)


class Team_Devs:
  def __init__(self, team_name, project_name, design, qa, devops, frontend, system, backend, product_owner):

      self.team_name = team_name
      self.project_name = project_name
      self.design = design
      self.qa = qa
      self.devops = devops
      self.frontend = frontend
      self.system = system
      self.backend = backend
      self.product_owner = product_owner

class Company:
    def __init__(self, sales_persons, share_holders, product_owners, dev_teams):

        self.sales_persons = sales_persons
        self.share_holders = share_holders
        self.product_owners = product_owners
        self.dev_teams = dev_teams


    def show(self):
        output = self.__dict__
        for person, list_persons in output.items():
            print(person)
            for person in list_persons:
                print(person.__dict__)
                print(person.stats.__dict__)



    #Building the company

i = 0
list_sales_persons = []
while i < 3:
    sp1 = "First_Name"
    sp2 = "Last_Name"
    sp3, sp4 = random.randint(1,10), random.randint(1,10)
    sales_persons = SalesPersons(str(sp1), str(sp2), sp3, sp4)
    list_sales_persons.append(sales_persons)
    i+=1



i = 0
list_share_holders = []
while i < 4:
    sh1 = "First_Name"
    sh2 = "Last_Name"
    sh3 = 25
    share_holders = ShareHolders(str(sh1), str(sh2), sh3)
    list_share_holders.append(share_holders)
    i+=1


i = 0
list_product_owners = []
while i < 2:
    po1 = "First_Name"
    po2 = "Last_Name"
    po3 = 2
    po4 = random.randint(1,10)
    product_owners = ProductOwners(str(po1), str(po2), po3, po4)
    list_product_owners.append(product_owners)
    i+=1


#Building the DEV TEAMS

#UX
senior_ux = Devs("Senior_name", "last_name", 7, 2, 7, 2, 2, 6, 9)
mid_ux =Devs("Mid_name", "last_name", 4, 1, 6, 2, 2, 6, 7)


#QA
senior_qa = Devs("Senior_qa", "last_name",9,4,5,2,3,9,3)
mid_qa = Devs("Mid_qa", "last_name",7,3,4,3,2,7,4)
junior_qa = Devs("junior_qa", "last_mane",2,2,1,1,3,5,2)

# DevOPS
senior_devops = Devs("senior_devops", "last_name",9,8,7,9,9,8,6)
junior_devops = Devs("junior_devops", "last_name",2,5,5,5,6,4,4)

# Frontend

senior_frontend = Devs("Senior_frontend", "last_name",9,4,9,5,6,6,7)
mid_frontend = Devs("mid_frontend", "last_name",7,5,7,6,7,6,7)
junior_frontend = Devs("jr_front", "last_name",2,4,5,4,4,3,5)

# Backend

senior_backend = Devs("Senior_backend", "last_name",9,9,6,6,7,6,2)
mid_backend = Devs("mid_backend", "last_name", 7,7,6,6,6,7,4)
junior_backend = Devs("jr_backend", "last_name",2,5,4,4,5,4,2)

system_engineer = Devs("system_engineer", "last_name",6,3,4,6,8,7,4)

company = Company(list_sales_persons, list_share_holders, list_product_owners,[senior_ux, mid_ux], [senior_qa, mid_qa, junior_qa],
                  [senior_devops, junior_devops], system_engineer, 3 * [senior_frontend], 2 * [mid_frontend], 3 * [junior_frontend],
                  4 * [senior_backend], 3 * [mid_backend], 5 * [junior_backend] )

company.show()