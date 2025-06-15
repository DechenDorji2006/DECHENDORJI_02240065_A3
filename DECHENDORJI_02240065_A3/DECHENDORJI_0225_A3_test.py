import unittest
from DECHENDORJI_02240065_A3 import Banking_function

class Test_Banking_System(unittest.TestCase):
    """Test cases for the Banking System. how it works us through the Banking_function class."""
    def setUp(self): # thhis method is called before each test, it is class method
        self.banking = Banking_function()
        self.personal_account = self.banking.create_new_account("Personal")
        self.business_account = self.banking.create_new_account("Business")
        self.personal_account.deposit_money(1000)
        self.business_account.deposit_money(500)

    def depositing_negative_amount_check(self): # this method checks if the deposit function works with negative amount
        self.assertEqual(self.personal_account.deposit_money(-100), "fund invalid.")

    def withdrawing_more_than_available_balance(self): # this method checks if the withdraw function works with more than available balance
        self.assertEqual(self.personal_account.withdraw(2000), "low balance")

    def zero_amount_transfer_check(self): # this method checks if the transfer function works with zero amount
        self.assertEqual(self.personal_account.transfer(0, self.business_account), "Invalid Transfer amount.")

    def negative_recharge_check(self): #    this method checks if the phone top-up function works with negative amount
        self.assertEqual(self.personal_account.phone_top_up(-50), "Invalid recharge amount.")

    def no_recipent_when_transfer_check(self): # this method checks if the transfer function works with no recipient
        with self.assertRaises(AttributeError):
            self.personal_account.transfer(100, None)

    def login_invalid_check(self): # this method checks if the login function works with invalid credentials
        self.assertIsNone(self.banking.login_account("wrongid", "wrongpasscode"))

    def no_account_delete_check(self): # this method checks if the delete function works with no account
        self.assertFalse(self.banking.delete_existing_account("00000"))

    def desposit_valid_check(self): #   this method checks if the deposit function works with valid amount
        self.assertEqual(self.business_account.deposit_money(200), "Deposit is successful.")
        self.assertEqual(self.business_account.Money_Balance, 700)

    def withdraw_valid_check(self): # this method checks if the withdraw function works with valid amount
        self.assertEqual(self.personal_account.withdraw(300), "Withdrawal successful.")
        self.assertEqual(self.personal_account.Money_Balance, 700)

    def transfering_valid_check(self): # this method checks if the transfer function works with valid amount
        self.assertEqual(self.personal_account.transfer(200, self.business_account), "Transfer completed.")
        self.assertEqual(self.personal_account.Money_Balance, 800)
        self.assertEqual(self.business_account.Money_Balance, 700)

    def recharge_valid_check(self): # this method checks if the phone top-up function works with valid amount
        self.assertEqual(self.personal_account.phone_top_up(100), "Phone is recharged, Phone balance: 100")
        self.assertEqual(self.personal_account.Money_Balance, 900)

    def test_delete_existing_account(self): # this method checks if the delete function works with an existing account
        acc_id = self.personal_account.Acct_ID
        self.assertTrue(self.banking.delete_existing_account(acc_id))
        self.assertNotIn(acc_id, self.banking.class_Accounts)

if __name__ == '__main__':
    unittest.main()
