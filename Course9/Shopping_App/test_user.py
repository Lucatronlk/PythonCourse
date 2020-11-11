import unittest
import os

from user import User

class TestUser(unittest.TestCase):
    def test_add_user(self):
        # setup

        # execution
        user = User('user1')
        message = user.save()


    # expectation
        was_user_created = True
        try:
            f = open('user_user1')
            f.close() #close the file if we manage to open it
        except:
            was_user_created = False # if we fai; we set it to false

        self.assertTrue(was_user_created)
        self.assertEqual('User added', message)

        #cleanup
        os.remove('user_user1')

    def test_user_already_exists(self):
        #setup
        f = open('user_user1', 'w') #create a file user_user1
        f.close() #close the file after we create it
        #execusion
        user = User('user1')
        message = user.save()

        #cleanup
        os.remove('user_user1')

        #assertion
        self.assertEqual('User already exists', message)


    def test_remove_user(self):
        #setup
        f = open('user_user1', 'w')
        f.close()


        #execution
        user = User ('user1')
        result = user.remove()

        #assertion
        self.assertTrue(result)


    def test_does_not_remove_user(self):
        #setup

        #execution
        user = User('user1')
        result = user.remove()

        #assertion
        self.assertFalse(result)

