import unittest
from bills_repository import BillRepository
from compute_bill import compute_price

class TestBill(unittest.TestCase):
    def test_bill(self):
        repo = BillRepository()
        bills = repo.get()

        actual_message = compute_price(bills[0])
        self.assertEqual('Billy has to pay 4.8$', actual_message)

        actual_message = compute_price(bills[5])
        self.assertEqual('Jeff has to pay 43.0$', actual_message)


if __name__ == '__main__':
    unittest.main()
