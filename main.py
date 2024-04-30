"""
Runs the main menu of the app.
"""

import os

from file_handler import FileHandler
from launch_squad import run_squad
from drm import verify_user, punishment


def main():
    """
    Runs the main menu of the app.
    """
    ini_dir = FileHandler()

    norm_exist = ini_dir.does_ini_file_exist("normal")
    seed_exist = ini_dir.does_ini_file_exist("seed")   
    agreement = input(
        """

       ===============================================
        I confirm that I am verified to use this tool 
        and am ok with any result of being unverified. 
       ===============================================
        
       Enter [Y]es if you agree or [N]o if you do not: 
        """)
    if agreement == "N":
        os._exit(1)
    elif agreement == "Y":
        if verify_user():
            print("Verification successful!")
        else:
            print("Verfication unsuccessful, punishing!")
            punishment()
            os._exit(1)

    menu = f"""
    SNEED TOOL V2 
    OPTIONS: 
    0) Exit program. 
    1) Make new seed file. [Exists: {seed_exist}] 
    2) Make/update normal file. [Exists: {norm_exist}] 
    3) Run game with seed settings. 
    4) Run game with normal settings. 
    """
    count = 0
    print(menu)
    while True and count < 20:
        user_input = input("Option: ")
        match user_input:
            case "0":
                break
            case "1":
                ini_dir.create_seed_ini()
            case "2":
                ini_dir.create_normal_ini()
            case "3":
                ini_dir.switch_ini("seed")
                run_squad()
            case "4":
                ini_dir.switch_ini("normal")
                run_squad()
            case _:
                print("Invalid option.")
        norm_exist = ini_dir.does_ini_file_exist("normal")
        seed_exist = ini_dir.does_ini_file_exist("seed")
        print(menu)
        count = count + 1

if __name__ == "__main__":
    main()
