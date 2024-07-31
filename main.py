"""
Runs the seeding application.
"""

import os
import argparse
import sys

from file_handler import FileHandler
from launch_squad import run_squad
from drm import verify_user, punishment
from const import CRACKED

def agreement_menu() -> None:
    """
    Handles the verification sub-menu and any related punishments.
    """
    if not CRACKED:
        agreement = input(
                """
            ===============================================
            I confirm that I am verified to use this tool 
            and am ok with any result of being unverified. 
            ===============================================
                
            Enter [yes] if you agree or [no] if you do not: 
                """)
        agreement_handler(agreement)




def agreement_handler(choice: str):
    """
    Handles program flow with agreements.
    """
    if choice.lower() == "no":
        os._exit(1)
    elif choice.lower() == "yes":
        if verify_user():
            print("Verification successful!")
        else:
            print("Verfication unsuccessful, punishing!")
            punishment()
            os._exit(1)

def get_file_status(ini_dir: FileHandler) -> list:
    """
    Retrieves file statuses.
    """
    return {'s': ini_dir.does_ini_file_exist("seed"),
            'n': ini_dir.does_ini_file_exist("normal")}

def print_menu(seed, normal) -> None:
    """
    Updates the menu with the status of the seed and normal files.
    """
    menu = f"""
        SNEED TOOL V2 
        OPTIONS: 
        0) Exit program. 
        1) Make new seed file. [Exists: {seed}] 
        2) Make/update normal file. [Exists: {normal}] 
        3) Run game with seed settings. 
        4) Run game with normal settings. 
        """
    print(menu)


def menu_handler(ini_dir: FileHandler):
    """
    Handles the looping main menu of the application.
    """
    agreement_menu()
    status = get_file_status(ini_dir)
    print_menu(status['s'], status['n'])
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
                ini_dir.switch_ini("seed")
                print(run_squad().format('seed'))
                break
            case "4":
                ini_dir.switch_ini("normal")
                print(run_squad().format('normal'))
                break
            case _:
                print("Invalid option.")
        status = get_file_status(ini_dir)
        print_menu(status['s'], status['n'])
        count = count + 1


def argument_handler()-> None:
    """
    Defines arguments for running the script and parses them.
    """
    parser = argparse.ArgumentParser(
            prog="seedtoolv2",
            description="a program that manages alternate setting profiles for Squad seeding"
        )
    if not CRACKED:
        parser.add_argument(
            'agree',
            type=str,
            choices=['yes', 'no'],
            help='whether you as a user are authorised to use this tool.'
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
    args = parser.parse_args()
    return args

def main():
    """
        Runs the main menu of the app.
    """
    ini_dir = FileHandler()
    if len(sys.argv) > 1:
        args = argument_handler()
        if not CRACKED:
            agreement_handler(args.agree)
        if args.make is not None:
            if args.make == 'normal':
                ini_dir.create_normal_ini()
            elif args.make == 'seed':
                ini_dir.create_seed_ini()
        elif args.run is not None:
            ini_dir.switch_ini(args.run)
            print(run_squad().format(args.run))
        elif args.status is not None:
            norm_exist = ini_dir.does_ini_file_exist("normal")
            seed_exist = ini_dir.does_ini_file_exist("seed")
            print(f'Seed file status: {seed_exist} | Normal file status: {norm_exist}')
    else:
        try:
            menu_handler(ini_dir)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt detected, closing tool.")
            os._exit(0)

if __name__ == "__main__":
    main()
