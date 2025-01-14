from enum import Enum, auto

class Role(Enum):
    USER = auto()
    SUPPORT = auto()
    ADMIN = auto()

def check_permission(role: Role, required_role: Role):
    if role == required_role or role == Role.ADMIN:
        return True
    return False
