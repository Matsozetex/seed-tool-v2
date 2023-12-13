from dataclasses import dataclass
from const import SEED_GAME_SETTINGS

@dataclass
class IniFile:
    ini_name: str
    ini_type: str
    ini_tag: str
    ini_dx: bool
    ini_content: str

    def __init__(self, ini_name: str, ini_dx: bool, ini_type: str, ini_tag: str):
        self.ini_name = ini_name
        self.ini_type = ini_type
        self.ini_dx = ini_dx
        self.ini_tag = ini_tag
        self.ini_content = ''

    def set_seed_content(self) -> None:
        ini_string = ''
        if(self.ini_type == "SEED_MODE"):
            ini_string = SEED_GAME_SETTINGS
            ini_string = ini_string.replace("{tag}", self.ini_tag).replace("{dx}", str(self.ini_dx) )
            self.ini_content = ini_string
      
        
