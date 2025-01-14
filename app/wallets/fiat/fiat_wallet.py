from datetime import datetime
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP

@dataclass
class FiatWallet:
    user_id: int | None
    wallet_id: int | None
    balance: Decimal | None
    iban: str | None = None   
    swift_code: str | None = None 
    routing_number: str | None = None 
    last_accessed: datetime | None = None
    encryption_key: str | None = None
    deposit_history: dict[str, Decimal] = field(default_factory=dict)
    withdrawal_history: dict[str, dict[str, Decimal]] = field(default_factory=dict)

    def add_deposit_to_history(self, date: datetime, amount: Decimal) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.deposit_history[formatted_date] = self.deposit_history.get(formatted_date, Decimal("0.00")) + amount

    def add_withdrawal_to_history(self, date: datetime, amount: Decimal, method: str) -> None:
        amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
        self.withdrawal_history.setdefault(formatted_date, {})[method] = amount

    def has_sufficient_funds(self, amount: Decimal) -> bool:
        return (self.balance or Decimal("0.00")) >= amount

    def increase_wallet_balance(self, amount: Decimal) -> None:
        if self.balance is None:
            raise ValueError("Wallet balance is None, cannot credit funds.")
        
        self.balance += amount
        self.balance = self.balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def decrease_wallet_balance(self, amount: Decimal) -> None:
        if self.balance is None:
            raise ValueError("Wallet balance is None, cannot perform withdrawal.")
        
        self.balance -= amount
        self.balance = self.balance.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    def update_last_accessed(self) -> None:
        self.last_accessed = datetime.now()

    def update_iban(self, new_iban: str):
        self.iban = new_iban

    def update_swift_code(self, new_swift_code: str):
        self.swift_code = new_swift_code

    def update_routing_number(self, new_routing_number: str):
        self.routing_number = new_routing_number


