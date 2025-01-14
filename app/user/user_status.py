from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class UserStatus:
    is_online: bool
    is_banned: bool
    is_inactive: bool
    ban_type: str | None   
    ban_reason: str | None 
    ban_duration: int | None
    ban_start_time: datetime | None 
    ban_end_time: datetime | None   

    def update_ban_status(self, is_banned: bool, ban_type: str, ban_reason: str, ban_duration: int | None = None):
        self.is_banned = is_banned
        self.ban_type = ban_type
        self.ban_reason = ban_reason
        self.ban_start_time = datetime.now()

        if ban_type == "temporary":
            if ban_duration is None:
                raise ValueError("Duration must be specified for a temporary ban.")
            self.ban_duration = ban_duration
            self.ban_end_time = self.ban_start_time + timedelta(days=ban_duration)

        elif ban_type == "permanent":
            self.ban_duration = None
            self.ban_end_time = None
        else:
            raise ValueError("Ban type must be 'temporary' or 'permanent'.")
        
        ban_duration_display = self.ban_duration if self.ban_type == 'temporary' else 'N/A'
        print(f"User banned: {is_banned}, Reason: {ban_reason}, Type: {ban_type}, Duration: {ban_duration_display}")

    def update_online_status(self, is_online: bool):
        self.is_online = is_online
        print(f"User Online: {is_online}.")

    def update_inactivity_status(self, last_login: datetime | None, inactivity_threshold_days: int = 30):
        if last_login is None:
            self.is_inactive = True 
        else:
            if datetime.now() - last_login > timedelta(days=inactivity_threshold_days):
                self.is_inactive = True
            else:
                self.is_inactive = False
        print(f"User inactivity: {self.is_inactive}.")
