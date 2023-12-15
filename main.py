from seed_file import SeedIniFile
from file_handler import FileHandler
from const import SETTING_DIR, GAME_NAME, SEED_MODE, NORMAL_MODE
import customtkinter
from ui_manager import App  

def check_ini_type() -> str:
        with open(SETTING_DIR / GAME_NAME) as file:
            file_contents = file.read()
        if( file_contents.find(SEED_MODE) >= 0):
            ini_type = SEED_MODE
        else:
            ini_type = NORMAL_MODE
        return ini_type

def main():
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = App()
    app.make_grid_layout()
    app.grid_settings_elements()
    app.mainloop()


if __name__ == "__main__":
    main()