from dataclasses import dataclass

from helpers.roles import Role

from app.user.user_bank import UserBank
from app.user.user_status import UserStatus
from app.user.user_history import UserHistory
from app.user.user_security import UserSecurity
from app.user.user_fingerprint import UserFingerprint

@dataclass
class User:
    id: int | None
    username: str
    email: str
    role: Role
    user_bank: UserBank
    user_status: UserStatus
    user_history: UserHistory
    user_security: UserSecurity
    user_fingerprint: UserFingerprint

    def update_username(self, new_username: str):
        self.username = new_username
        print(f"Username updated to {new_username}.")

    def update_email(self, new_email: str):
        self.email = new_email
        print(f"Email updated to {new_email}.")

    def update_role(self, new_role: Role):
        self.role = new_role
        print(f"Role updated to {new_role}.")

    def update_user_bank(self, new_user_bank: UserBank):
        self.user_bank = new_user_bank
        print("Bank information updated.")

    def update_user_status(self, new_user_status: UserStatus):
        self.user_status = new_user_status
        print("Status updated.")

    def update_user_history(self, new_user_history: UserHistory):
        self.user_history = new_user_history
        print("User history updated.")

    def update_user_security(self, new_user_security: UserSecurity):
        self.user_security = new_user_security
        print("Security info updated.")

    def update_user_fingerprint(self, new_user_fingerprint: UserFingerprint):
        self.user_fingerprint = new_user_fingerprint
        print("User fingerprint updated.")