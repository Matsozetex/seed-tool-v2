"""
Defines behaviour of CLI interface.
"""

import user_actions

from file_handler import FileHandler

def print_menu(seed, normal, server) -> None:
    """
    Updates the menu with the status of the seed and normal files.
    """
    menu = f"""
        SNEED TOOL V2 
        OPTIONS: 
        0) Exit program. 
        1) Make/reset seed file. [Exists: {seed}] 
        2) Make/update normal file. [Exists: {normal}] 
        3) Set desired server to auto-seed. [Server: {server}]
        4) Run game with auto-seed settings.
        5) Run game with seed settings. 
        6) Run game with normal settings. 
        """
    print(menu)


def menu_handler(ini_dir: FileHandler):
    """
    Handles the looping main menu of the application.
    """
    status = user_actions.get_file_status(ini_dir)
    print_menu(status['s'], status['n'], status['h'])
    count = 0
    while True and count < 20:
        user_input = input("Option: ")
        match user_input:
            case "0":
                break
            case "1":
                user_actions.make_seed(ini_dir)
            case "2":
                user_actions.make_normal(ini_dir)
            case "3":
                user_actions.update_server(ini_dir)
            case "4":
                user_actions.run_auto_seed(ini_dir)
                break
            case "5":
                user_actions.run_seed(ini_dir)
                break
            case "6":
                user_actions.run_normal(ini_dir)
                break
            case _:
                print("Invalid option.")
        status = user_actions.get_file_status(ini_dir)
        print_menu(status['s'], status['n'], status['h'])
        count = count + 1
