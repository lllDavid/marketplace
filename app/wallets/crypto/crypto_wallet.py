from datetime import datetime
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP

@dataclass
class CryptoWallet:
    user_id: int | None
    wallet_id: int | None
    wallet_address: str | None
    coins: dict[str, Decimal] = field(default_factory=dict)
    total_coin_value: Decimal | None = None
    last_accessed: datetime | None = None
    encryption_key: str | None = None
    deposit_history: dict[str, Decimal] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, Decimal]] = field(default_factory=dict)

    def add_deposit_to_history(self, date: datetime, amount: Decimal) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.deposit_history[formatted_date] = self.deposit_history.get(formatted_date, Decimal("0.00")) + amount
        # TODO Always doubles the actual amount

    def add_withdrawal_to_history(self, date: datetime, amount: Decimal, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.withdrawal_history.setdefault(formatted_date, {})[method] = amount

    def calculate_total_coin_value(self) -> Decimal:
        total_value = sum(self.coins.values(), Decimal(0)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.total_coin_value = total_value
        return total_value

    def add_coins(self, coin: str, amount: Decimal, date: datetime) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to add must be positive.")
        self.coins[coin] = self.coins.get(coin, Decimal("0.00")) + amount
        self.add_deposit_to_history(date, amount)

    def remove_coins(self, coin: str, amount: Decimal, date: datetime, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if amount <= Decimal("0.00"):
            raise ValueError("Amount to subtract must be positive.")
        if coin not in self.coins or self.coins[coin] < amount:
            raise ValueError("Insufficient coins or coin does not exist.")
        self.coins[coin] -= amount
        self.add_withdrawal_to_history(date, amount, method)

    def update_wallet_address(self, new_address: str) -> None:
        if not new_address:
            raise ValueError("Wallet address cannot be empty.")
        self.wallet_address = new_address

    def update_encryption_key(self, new_key: str) -> None:
        if not new_key:
            raise ValueError("Encryption key cannot be empty.")
        self.encryption_key = new_key

    def update_last_accessed(self):
        self.last_accessed = datetime.now()
