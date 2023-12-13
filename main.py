from seed_file import SeedIniFile
from file_handler import FileHandler
from const import SETTING_DIR

def main():
    SeedFile = SeedIniFile(False,  "[ABG]")
    fh = FileHandler()
    fh.change_file_contents()



if __name__ == "__main__":
    main()