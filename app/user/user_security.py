from random import randint
from dataclasses import dataclass

from pyotp import TOTP, random_base32
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError

@dataclass
class UserSecurity:
    password_hash: str
    two_factor_enabled: bool
    two_factor_secret_key: str | None 
    two_factor_backup_codes: set | None 
    two_factor_backup_codes_hash: set | None 

    @staticmethod
    def hash_password(password: str, time_cost: int = 4, memory_cost: int = 102400, parallelism: int = 8):
        ph = PasswordHasher(time_cost=time_cost, memory_cost=memory_cost, parallelism=parallelism)
        hashed_password = ph.hash(password)
        return hashed_password
    
    @staticmethod
    def validate_password_hash(attempt_password: str, db_hash: str) -> bool:
        ph = PasswordHasher()
        try:
            ph.verify(db_hash, attempt_password)
            return True
        except VerificationError:
            return False
        
    @staticmethod
    def generate_backup_codes(num_codes: int = 6) -> set:
        return {str(randint(100000, 999999)) for _ in range(num_codes)}
    
    @staticmethod
    def hash_backup_codes(backup_codes: set) -> set:
        ph = PasswordHasher()  
        return {ph.hash(code) for code in backup_codes}
        
    def generate_2fa_secret_key(self):
        totp = TOTP(random_base32())
        self.secret_key = totp.secret

    def generate_2fa_qr_code(self, username: str):
        totp = TOTP(self.secret_key)
        uri = totp.provisioning_uri(username, issuer_name="Marketplace")
        print(f"Scan this QR code in your 2FA app: {uri}")

    def verify_2fa_code(self, user_provided_code: str) -> bool:
        if not self.two_factor_secret_key:
            return False 
        
        totp = TOTP(self.two_factor_secret_key)  
        
        return totp.verify(user_provided_code)  
    