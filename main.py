from seed_file import SeedIniFile
from file_handler import FileHandler
from const import SETTING_DIR

def main():
    SeedFile = SeedIniFile(False, "SEED_MODE", "[ABG]")
    fh = FileHandler()

    fh.create_normal_file()


if __name__ == "__main__":
    main()