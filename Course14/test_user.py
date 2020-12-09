import unittest
from voting import User

class TestVoting(unittest.TestCase):
    def test_user_has_not_voted(self):
        #setup

        #execution
        user = User('name1')
        has_voted = user.has_user_already_voted()
        #assertion
        self.assertFalse(has_voted)


if __name__ == '__main__':
    unittest.main()
