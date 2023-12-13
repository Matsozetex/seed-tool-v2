from dataclasses import dataclass
from const import SEED_GAME_SETTINGS

@dataclass
class IniFile:
    clan_tag: str
    is_seed: bool
    file_path: str
    file_contents: str

    def __init__(self, clan_tag: str, is_seed: bool, file_path: str):
        self.clan_tag = clan_tag
        self.ini_type = is_seed
        self.file_path = file_path
        self.file_contents = SEED_GAME_SETTINGS.replace("{tag}", self.clan_tag)
