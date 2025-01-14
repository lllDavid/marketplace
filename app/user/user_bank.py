from datetime import datetime
from dataclasses import dataclass

@dataclass
class UserBank:
    bank_name: str | None
    account_holder: str | None
    account_number: str | None
    routing_number: str | None
    iban: str | None
    swift_code: str | None
    date_linked: datetime | None

    def update_bank_name(self, new_bank_name: str) -> None:
        self.bank_name = new_bank_name

    def update_account_holder(self, new_holder: str) -> None:
        self.account_holder = new_holder

    def update_account_number(self, new_account_number: str) -> None:
        self.account_number = new_account_number

    def update_routing_number(self, new_routing_number: str) -> None:
        self.routing_number = new_routing_number

    def update_iban(self, new_iban: str) -> None:
        self.iban = new_iban

    def update_swift_code(self, new_swift_code: str) -> None:
        self.swift_code = new_swift_code

    def update_date_linked(self, new_date_linked: datetime) -> None:
        self.date_linked = new_date_linked
