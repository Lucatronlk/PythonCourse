import unittest
from voting import User
from unittest import mock

class TestVoting(unittest.TestCase):
    @mock.patch('voting.User.read_file', return_value = ['name2\n'])
    def test_user_has_not_voted(self, read_file):
        #setup - manually
        #execution
        user = User('name1')
        has_voted = user.user_already_voted()
        #assertion
        self.assertFalse(has_voted)

    @mock.patch('voting.User.read_file', return_value=['name2\n'])
    def test_user_voted(self, read_file):
        #setup - manually
        #execution
        user = User('name2')
        has_voted = user.user_already_voted()
        #assertion
        self.assertTrue(has_voted)


if __name__ == '__main__':
    unittest.main()
