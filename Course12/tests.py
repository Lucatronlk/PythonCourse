import unittest
from main import get_user_and_pass,EmptyCredentials, Credentials


class TestPassword(unittest.TestCase):
    def test_get_user_and_password(self):
        # user, password = get_user_and_pass('netflix')
        credentials = get_user_and_pass('netflix')
        expected_credentials = Credentials('lucatronlk', 'parola2')
        self.assertEqual(expected_credentials.__dict__, credentials.__dict__)

        # self.assertEqual('lucatronlk', user)
        # self.assertEqual('parola2', password)
        # self.assertEqual( 'lucatronlk', credentials.user)
        # self.assertEqual('parola2', credentials.password)



    def test_get_not_configured_website(self):
        #execute, try to get info for a site not in the dictonary
        # user, password = get_user_and_pass('emag')
         credentials = get_user_and_pass('emag')

         self.assertEqual(EmptyCredentials().__dict__, credentials.__dict__)
         # self.assertEqual('', credentials.user)
         # self.assertEqual('', credentials.password)