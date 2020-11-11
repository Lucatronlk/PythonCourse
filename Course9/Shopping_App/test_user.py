import unittest

import self as self
from user import User

class TestUser(unittest.TestCase):
    def test_add_user(self):
        # setup

        # execution
    user = User('user1')
    user.save()


    # expectation
    was_user_created = True
    try:
      f = open('user_user1')
      f.close() #close the file if we manage to open it
    except:
        was_user_created = False # if we fai; we set it to false

    self.assertTrue(was_user_created)
