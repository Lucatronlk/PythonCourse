import unittest
from steam import Client, GameCollection


class TestClient(unittest.TestCase):
    def test_add_money(self):
        #set up
        client = Client('user1')
        #execition
        client.add_money(100)
        #assertion
        self.assertEqual(100, client.money)


    def test_return_false_if_to_much_money_was_added(self):
        # set up
        client = Client('user1')
        #execition
        response = client.add_money(700)
        #assertion
        self.assertEqual(False, response)
        self.assertEqual(0, client.money)


    def test_buy_games(self):
        client = Client('user1')
        client.add_money(300)
        list = ['Cyberpunk', 'Minecraft', 'Sims']
        #execution
        client.buy_games(list, 'ADA')
        #assertion
        self.assertEqual(206, client.money)