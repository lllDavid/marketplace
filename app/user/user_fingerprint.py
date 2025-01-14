from dataclasses import dataclass

@dataclass
class UserFingerprint:
    username_history: set[str]
    email_address_history: set[str]
    mac_address: str | None 
    associated_ips: dict[str, int] | None
    device_id: str | None 
    device_type: str | None
    device_manufacturer: str | None 
    device_model: str | None 
    screen_resolution: str | None 
    geolocation_country: str | None 
    geolocation_city: str | None 
    geolocation_latitude: float | None
    geolocation_longitude: float | None 
    avg_login_frequency: dict[str, float] | None
    avg_session_duration: dict[str, float] | None 
    behavioral_biometrics: dict[str, float] | None 
    browser_info: str | None 
    os_name: str | None 
    os_version: str | None
    vpn_usage: bool | None 
    user_preferences: dict[str, str] | None 
    user_agent: str | None 
    two_factor_enabled: bool | None 

    def update_username_history(self, username: str):
        self.username_history.add(username)

    def update_email_address_history(self, email: str):
        self.email_address_history.add(email)

    def update_mac_address(self, mac_address: str):
        self.mac_address = mac_address

    def update_associated_ips(self, ip_address: str, count: int = 1):
        if self.associated_ips is None:
            self.associated_ips = {}
        self.associated_ips[ip_address] = self.associated_ips.get(ip_address, 0) + count

    def update_avg_login_frequency(self, day: str, frequency: float):
        if self.avg_login_frequency is None:
            self.avg_login_frequency = {}
        self.avg_login_frequency[day] = frequency

    def update_avg_session_duration(self, day: str, duration: float):
        if self.avg_session_duration is None:
            self.avg_session_duration = {}
        self.avg_session_duration[day] = duration

    def update_geolocation(self, country: str, city: str, latitude: float, longitude: float):
        self.geolocation_country = country
        self.geolocation_city = city
        self.geolocation_latitude = latitude
        self.geolocation_longitude = longitude

    def update_browser_info(self, browser_info: str):
        self.browser_info = browser_info

    def update_os_info(self, os_name: str, os_version: str):
        self.os_name = os_name
        self.os_version = os_version

    def update_device_info(self, device_type: str, device_manufacturer: str, device_model: str):
        self.device_type = device_type
        self.device_manufacturer = device_manufacturer
        self.device_model = device_model

    def update_user_preferences(self, preference_key: str, preference_value: str):
        if self.user_preferences is None:
            self.user_preferences = {}
        self.user_preferences[preference_key] = preference_value

    def update_user_agent(self, user_agent: str):
        self.user_agent = user_agent

    def update_device_id(self, device_id: str):
        self.device_id = device_id

    def update_screen_resolution(self, resolution: str):
        self.screen_resolution = resolution

    def update_two_factor_enabled(self, enabled: bool):
        self.two_factor_enabled = enabled

    def update_vpn_usage(self, vpn_usage: bool):
        self.vpn_usage = vpn_usage

    def update_behavioral_biometrics(self, biometrics: dict[str, float]):
        if self.behavioral_biometrics is None:
            self.behavioral_biometrics = {}
        self.behavioral_biometrics.update(biometrics)


