from dataclasses import dataclass
from const import SEED_GAME_SETTINGS

@dataclass
class SeedIniFile:
    ini_tag: str =""
    ini_dx12: bool = ""
    ini_content: str = ""

    def __init__(self,  ini_dx12: bool, ini_tag: str):
        self.ini_dx12 = ini_dx12
        self.ini_tag = ini_tag
        self.ini_content = ''

    def set_content(self) -> None:
        ini_string = SEED_GAME_SETTINGS
        ini_string = ini_string.replace("{tag}", self.ini_tag).replace("{dx}", str(self.ini_dx12) )
        self.ini_content = ini_string
      
    def set_tag(self, new_tag: str) -> None:
        if(len(new_tag) <= 7):
            self.ini_tag = new_tag 
        

    def set_dx(self, new_dx: bool) -> None:
        self.ini_dx12 = new_dx
    
    