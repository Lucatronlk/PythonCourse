import unittest
import json

class TestJson(unittest.TestCase):
    def test_json(self):
        list = [1, 2, 3, 4]
        json_list = json.dumps(list) #we encode the list to JSON format
        print(json_list)

        self.assertEqual('[1, 2, 3, 4]', json_list)

        decoded_list = json.loads(json_list) #decode

        self.assertEqual(list, decoded_list)

