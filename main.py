from seed_file import SeedIniFile
from file_handler import FileHandler
from const import SETTING_DIR, GAME_NAME, SEED_MODE, NORMAL_MODE
import customtkinter

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

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("800x450")
    app.minsize(800,450)
    app.maxsize(800,450)
    
    frame_settings = customtkinter.CTkFrame(master=app, width=150, height=400, corner_radius=20, bg_color="yellow")
    frame_file = customtkinter.CTkFrame(master=app, width=500, height=400, corner_radius=20, bg_color="yellow")
    frame_action = customtkinter.CTkFrame(master=app, width=150, height=400, corner_radius=20, bg_color="yellow")
    
    frame_settings.grid(column=0, row= 0)
    frame_file.grid(column=1, row= 0)
    frame_action.grid(column=2, row= 0)


    app.mainloop()



if __name__ == "__main__":
    main()