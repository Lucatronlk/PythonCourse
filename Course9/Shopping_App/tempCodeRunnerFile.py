
import unittest

class TestUser(unittest.TestCase):

    def test_true(self):
        self.assertEqual(True, True)

    def test_false(self):
        self.assertEqual(True, False, msg='error, True is not equal to False')
