from const import SETTING_DIR

def check_ini_type() -> str:
        with open(SETTING_DIR / 'GameUserSettings.ini') as file:
            file_contents = file.read()
        if( file_contents.find('SEED_MODE') >= 0):
            ini_type = "SEED_MODE"
        else:
            ini_type = "NORMAL_MODE"
        return ini_type

class FileHandler: 

    def __init__(self) -> None:
        pass

    def create_normal_file(self) -> bool:
        # Create the initial normal file for the tool and save it to the local directory
        # Check if the file is normal
        if(check_ini_type() == "NORMAL_MODE"):
            with open(SETTING_DIR / 'GameUserSettings.ini') as file:
                file_contents = file.read()
                with open(SETTING_DIR / "NormalGameUserSettings.ini", "x") as norm_file:
                    norm_file.write(file_contents)
            result = True
        else:
            result = False
        return result

    def create_seed_file(self,file_content) -> bool:
        result = False
        # Create the initial seed file for the tool and save it to the local directory
        with open(SETTING_DIR / "NormalGameUserSettings.ini", "x") as seed_file:
            seed_file.write(file_content)
            result = True
        return result

    def update_normal_file():
        # If mode is non-seed, update the stored normal file with current active settings
        pass
    def update_seed_file():
        # Update current stored seed file with new inputs from user
        pass
    def change_file_settings():
        # Change the active setting file with the new settings from seed or normal
        pass
