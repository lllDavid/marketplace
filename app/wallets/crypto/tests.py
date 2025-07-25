import unittest
from decimal import Decimal
from datetime import datetime

from crypto_wallet import CryptoWallet  

class TestCryptoWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = CryptoWallet(
            user_id=1,
            wallet_id=123,
            wallet_address="initial_address",
            coins={},
            total_coin_value=None,
            last_accessed=None,
            encryption_key="init_key",
            deposit_history={},
            withdrawal_history={}
        )
        self.now = datetime(2025, 7, 7, 12, 0, 0)

    def test_add_deposit_to_history_new_date(self):
        self.wallet.add_deposit_to_history(self.now, Decimal("10.005"))
        key = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertIn(key, self.wallet.deposit_history)
        self.assertEqual(self.wallet.deposit_history[key], Decimal("10.01"))

    def test_add_deposit_to_history_existing_date(self):
        key = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.wallet.deposit_history[key] = Decimal("5.00")
        self.wallet.add_deposit_to_history(self.now, Decimal("2.345"))
        self.assertEqual(self.wallet.deposit_history[key], Decimal("7.35"))

    def test_add_withdrawal_to_history(self):
        method = "bank_transfer"
        self.wallet.add_withdrawal_to_history(self.now, Decimal("7.345"), method)
        key = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertIn(key, self.wallet.withdrawal_history)
        self.assertEqual(self.wallet.withdrawal_history[key][method], Decimal("7.35"))

    def test_calculate_total_coin_value(self):
        self.wallet.coins = {
            "BTC": Decimal("0.123456789"),
            "ETH": Decimal("2.987654321")
        }
        self.wallet.calculate_total_coin_value()
        expected_total = (Decimal("0.123456789") + Decimal("2.987654321")).quantize(Decimal("0.01"))
        self.assertEqual(self.wallet.total_coin_value, expected_total)

    def test_add_coins_valid(self):
        self.wallet.add_coins("BTC", Decimal("1.234567890123456789"), self.now)
        self.assertIn("BTC", self.wallet.coins)
        self.assertEqual(self.wallet.coins["BTC"], Decimal("1.234567890123456789"))
        key = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertIn(key, self.wallet.deposit_history)

    def test_add_coins_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.wallet.add_coins("BTC", Decimal("-0.01"), self.now)

    def test_remove_coins_valid(self):
        self.wallet.coins = {"BTC": Decimal("2.000000000000000000")}
        self.wallet.remove_coins("BTC", Decimal("1.000000000000000000"), self.now, "withdrawal_method")
        self.assertEqual(self.wallet.coins["BTC"], Decimal("1.000000000000000000"))
        key = self.now.strftime('%Y-%m-%d %H:%M:%S')
        self.assertIn(key, self.wallet.withdrawal_history)
        self.assertEqual(self.wallet.withdrawal_history[key]["withdrawal_method"], Decimal("1.00"))

    def test_remove_coins_insufficient(self):
        self.wallet.coins = {"BTC": Decimal("0.5")}
        with self.assertRaises(ValueError):
            self.wallet.remove_coins("BTC", Decimal("1.0"), self.now, "withdrawal_method")

    def test_remove_coins_invalid_amount(self):
        self.wallet.coins = {"BTC": Decimal("2")}
        with self.assertRaises(ValueError):
            self.wallet.remove_coins("BTC", Decimal("-1"), self.now, "withdrawal_method")

    def test_remove_coins_nonexistent_coin(self):
        with self.assertRaises(ValueError):
            self.wallet.remove_coins("ETH", Decimal("1"), self.now, "withdrawal_method")

    def test_update_wallet_address_valid(self):
        new_address = "new_address_123"
        self.wallet.update_wallet_address(new_address)
        self.assertEqual(self.wallet.wallet_address, new_address)

    def test_update_wallet_address_empty(self):
        with self.assertRaises(ValueError):
            self.wallet.update_wallet_address("")

    def test_update_encryption_key_valid(self):
        new_key = "new_key_456"
        self.wallet.update_encryption_key(new_key)
        self.assertEqual(self.wallet.encryption_key, new_key)

    def test_update_encryption_key_empty(self):
        with self.assertRaises(ValueError):
            self.wallet.update_encryption_key("")

    def test_update_last_accessed(self):
        before_update = datetime.now()
        self.wallet.update_last_accessed()
        after_update = self.wallet.last_accessed
        self.assertTrue(after_update >= before_update)

if __name__ == "__main__":
    unittest.main()