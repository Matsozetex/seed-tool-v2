from const import SETTING_DIR, SEED_NAME, GAME_NAME, NORMAL_NAME, NORMAL_MODE, SEED_MODE
from os.path import isfile



class FileHandler: 
    def __init__(self) -> None:
        pass

    def create_seed_file(self,file_content) -> bool:
        # For the case of a new user with no seed file, make a new one 
        result = False
        with open(SETTING_DIR / SEED_NAME, "x") as seed_file:
            seed_file.write(file_content)
            result = True
        return result

    def update_normal_file(self, file_type) -> bool:
        """
        Check if active == normal. Then whether it exists, if it exists, rewrite it, if it doesn't make and write to it.
        """
        if(file_type == NORMAL_MODE):
            # If normal file already exists, we want to write
            if (isfile(SETTING_DIR / NORMAL_NAME)):
                mode = "w"
            # If normal file doesn't exist, we want to create
            else:
                mode = "x"
            with open(SETTING_DIR / GAME_NAME, "r") as file:
                    file_contents = file.read()
                    with open(SETTING_DIR / NORMAL_NAME, mode) as norm_file:
                        norm_file.write(file_contents)
            result = True
        else:
            result = False
        return result
    

    def update_seed_file(self, file_content, file_type) -> bool:
        if(file_type == SEED_MODE):
            if(isfile(SETTING_DIR / SEED_NAME)):
                result = False
            else:
                with open(SETTING_DIR / SEED_NAME, "w") as seed_file:
                    seed_file.write(file_content)
            result = True
        else:
            result = False
        # Update current stored seed file with new inputs from user
        return result
    
    def change_file_contents(self, new_mode) -> bool:
        if(new_mode == SEED_MODE):
            file_to_copy = SEED_NAME
        else:
            file_to_copy = NORMAL_NAME
        try:
            with open(SETTING_DIR / file_to_copy, 'r')  as file_to_read:
                file_contents = file_to_read.read()
                with open (SETTING_DIR / GAME_NAME, 'w') as file_to_write:
                    file_to_write.write(file_contents)
                    result = True
        except:
            result = False
        return result
    