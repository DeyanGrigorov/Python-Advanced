class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount):
        if account.balance + amount < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, other):
        new_acc = Account(self.owner + '&' + other.owner, self.amount + other.amount)
        new_acc._transactions = self._transactions + other._transactions
        return new_acc


import unittest


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('Deyan', 100)

    def test_add_transaction_invalid_type(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction(50.20)

    def test_add_transaction(self):
        self.assertEqual(len(self.account._transactions), 0)
        self.account.add_transaction(50)
        self.assertEqual(len(self.account._transactions), 1)

    def test_balance_property(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

    def test_validate_transaction_raises_exception_less_than_zero(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, -102)

    def test_validate_transaction(self):
        result = Account.validate_transaction(self.account, 100)
        self.assertEqual(result, 'New balance: 200')

    def test_validate_transaction_is_staticmethod(self):
        pass

    def test_custom_str(self):
        res = str(self.account)
        self.assertEqual(res, 'Account of Deyan with starting amount: 100')

    def test_custom_repr(self):
        res = repr(self.account)
        self.assertEqual(res, 'Account(Deyan, 100)')

    def test_custom_len(self):
        self.account.add_transaction(50)
        res = len(self.account)
        self.assertEqual(res, 1)

    def test_custom_iter(self):
        self.account.add_transaction(50)
        self.account.add_transaction(50)
        for t in self.account:
            self.assertEqual(t, 50)

    def test_custom_get_item(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        res = self.account[1]
        self.assertEqual(res, 150)

    def test_custom_gt(self):
        account_2 = Account('Test', 50)
        self.assertGreater(self.account, account_2)
        self.assertTrue(self.account > account_2)

    def test_custom_ge(self):
        account_2 = Account('Test', 50)
        self.assertGreaterEqual(self.account, account_2)
        self.assertGreaterEqual(self.account, self.account)


    def test_custom_add(self):
        account_2 = Account('Test', 50)
        account_3 = self.account + account_2
        self.assertEqual(repr(account_3), f"Account(Deyan&Test, 150)")
        self.assertEqual(account_3.balance, 150)
        self.assertEqual(account_3.owner, 'Deyan&Test')

    def test_validate_transaction_is_static_method(self):
        import types
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_reversed_method(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        res = list(reversed(self.account))
        self.assertEqual(res, [150, 50])

    def test_validate_transaction_is_static(self):
        self.assertIs(type(self.account.validate_transaction), type(lambda :None))

if __name__ == '__main__':
    unittest.main()