"""
Runs the seeding application.
"""

import os
import argparse
import sys
from time import sleep
from file_handler import FileHandler
from launch_squad import run_squad
from mouse import make_movements
from const import LOAD_TIMER

def get_file_status(ini_dir: FileHandler) -> list:
    """
    Retrieves file statuses.
    """
    return {'s': ini_dir.does_ini_file_exist("seed"),
            'n': ini_dir.does_ini_file_exist("normal"),
            'h': ini_dir.get_server_name()}

def print_menu(seed, normal, server) -> None:
    """
    Updates the menu with the status of the seed and normal files.
    """
    menu = f"""
        SNEED TOOL V2 
        OPTIONS: 
        0) Exit program. 
        1) Make new seed file. [Exists: {seed}] 
        2) Make/update normal file. [Exists: {normal}] 
        3) Set desired server to run. [Server: {server}]
        4) Run game with auto-seed settings.
        5) Run game with seed settings. 
        6) Run game with normal settings. 
        """
    print(menu)


def menu_handler(ini_dir: FileHandler):
    """
    Handles the looping main menu of the application.
    """
    status = get_file_status(ini_dir)
    print_menu(status['s'], status['n'], status['h'])
    count = 0
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
                ini_dir.update_desired_server()    
            case "4":
                ini_dir.switch_ini("seed")
                run_squad()
                print("Running squad in Seed mode")
                sleep(LOAD_TIMER)
                make_movements(ini_dir.get_server_name())
                break
            case "5":
                ini_dir.switch_ini("seed")
                run_squad()
                print("Running squad in Seed mode")
                break
            case "6":
                ini_dir.switch_ini("normal")
                run_squad()
                print("Running squad in Seed mode")
                break
            case _:
                print("Invalid option.")
        status = get_file_status(ini_dir)
        print_menu(status['s'], status['n'], status['h'])
        count = count + 1


def argument_handler()-> None:
    """
    Defines arguments for running the script and parses them.
    """
    parser = argparse.ArgumentParser(
            prog="seedtoolv2",
            description="a program that manages alternate setting profiles for Squad seeding"
        )
    group = parser.add_argument_group(
        'file operation commands', 
        'commands that execute file operations to faciltiate squad seeding'
        )
    exclusive_group = group.add_mutually_exclusive_group(required=True)
    exclusive_group.add_argument(
        '-m',
        '--make', 
        type=str,
        choices=['seed', 'normal'],
        help='make or update the alternate profiles'
        )
    exclusive_group.add_argument(
        '-r', 
        '--run', 
        type=str,
        choices=['seed', 'normal'],
        help='run the game in the alternate mode'
        )
    exclusive_group.add_argument(
        '-s',
        '--status',
        help='checks status of alternate profiles',
        action='store_const',
        const=1
    )
    exclusive_group.add_argument(
        '-a',
        '--auto',
        help='run the game with auto seed modes',
        action='store_const',
        const=1
    )
    exclusive_group.add_argument(
        '-M',
        '--host',
        help='sets the default server to connect to, the more accurate name the better',
        action='store_const',
        const=1
    )
    args = parser.parse_args()
    return args

def main():
    """
        Runs the main menu of the app.
    """
    ini_dir = FileHandler()
    if len(sys.argv) > 1:
        args = argument_handler()
        if args.make is not None:
            if args.make == 'normal':
                ini_dir.create_normal_ini()
            elif args.make == 'seed':
                ini_dir.create_seed_ini()
        elif args.run is not None and (args.run == 'normal' or args.run == 'seed'):
            ini_dir.switch_ini(args.run)
            run_squad()
            print(f"Running squad in {args.run} mode")
        elif args.host is not None:
            ini_dir.update_desired_server()   
        elif args.status is not None:
            norm_exist = ini_dir.does_ini_file_exist("normal")
            seed_exist = ini_dir.does_ini_file_exist("seed")
            server_name = ini_dir.get_server_name()
            print(f'Seed file status: {seed_exist} | Normal file status: {norm_exist} | Current desired server: {server_name}')
        elif args.auto is not None:
            ini_dir.switch_ini('seed')
            run_squad()
            print("Running squad in seed mode")
            sleep(LOAD_TIMER)
            make_movements(ini_dir.get_server_name())
    else:
        try:
            menu_handler(ini_dir)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected, closing tool.")
            os._exit(0)

if __name__ == "__main__":
    main()
