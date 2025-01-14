from dataclasses import dataclass

@dataclass
class Version:
    app_name:str = "Marketplace"
    app_version:str = "1.0.0"
    
    def update_name(self) -> str:
        name = input("New name:")
        self.app_name = name
        return name
    
    def update_version(self) -> str:
        version = input("New version: ")
        self.app_version = version
        return version
