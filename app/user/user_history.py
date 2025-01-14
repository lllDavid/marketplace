from datetime import datetime
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

@dataclass
class UserHistory:
    login_count: int 
    last_login: datetime | None
    failed_login_count: int 
    last_failed_login: datetime | None 
    created_at: datetime | None 
    updated_at: datetime | None 
    transaction_history: dict[str, Decimal] | None 

    def increment_login_count(self):
        self.login_count += 1
        self.update_updated_at()
    
    def update_last_login(self):
        self.last_login = datetime.now()
        self.update_updated_at()

    def increment_failed_login_count(self):
        self.failed_login_count += 1
        self.update_updated_at()

    def update_last_failed_login(self):
        self.last_failed_login = datetime.now()
        self.update_updated_at()

    def reset_failed_login_count(self):
        self.failed_login_count = 0
        self.update_updated_at()

    def initialize_created_at(self):
        self.created_at = datetime.now()

    def update_updated_at(self):
        self.updated_at = datetime.now()

    def update_transaction_history(self, transaction_id: str, amount: Decimal):
        if self.transaction_history is None:
            self.transaction_history = {}
        amount = amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        self.transaction_history[transaction_id] = amount
        self.update_updated_at()
