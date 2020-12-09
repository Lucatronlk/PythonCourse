# make a public voting system
# there are 100 users who can vote (name0, name1, ..., name 99)
# there are 4 parties which can be voted (party0, party1, party2, party3)
# register the votes in a file, w/o the user who voted
# register the users who voted in a file so a user can't vote 2 times

class User:
  def __init__(self, name):
    #save to object
    self.name = name

  def vote(self, party_id):
      if self.user_already_voted():
        return

      self.register_the_vote(party_id)
      self.register_to_users_who_voted()

  def user_already_voted(self):
      user_who_voted = self.read_file()
      has_user_already_voted = False
      # print(user_who_voted)
      # check if the user already voted
      if (self.name + '\n') in user_who_voted:
          print('User ' + self.name + ' already voted')
          has_user_already_voted = True
      return has_user_already_voted

  def read_file(self):
      # create a File object, to read users.txt
      read_users = open('users.txt')
      # read the file with readlines(), receive a list with the strings frm each line
      user_who_voted = read_users.readlines()
      # close the file
      read_users.close()
      return user_who_voted

  def write_file(self, vote):
      # create a File Object, to append the votes ( write at the end )
      votes_file = open('votes.txt', 'a')
      # convert party_id to stringA
      votes_file.write(vote)
      # close the file
      votes_file.close()

  def register_the_vote(self, party_id):
      # convert party_id to string
      self.write_file(str(party_id) + "\n")


  def register_to_users_who_voted(self):
      # create a File Objecty to write the users who voted
      users_file = open('users.txt', 'a')
      # write the name of the users
      users_file.write(self.name + "\n")
      # close the file
      users_file.close()


class Party:
    def __init__(self, id):
     self.id = id
     self.votes = 0

