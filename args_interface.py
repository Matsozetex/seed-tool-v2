"""
Defines behaviour of argument controls.
"""

import argparse
import user_actions
from file_handler import FileHandler

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

def argument_logic(args, handler: FileHandler) -> None:
    """
    Defines switching logic with related functions.
    """
    args = argument_handler()
    if args.make is not None:
        if args.make == 'normal':
            user_actions.make_normal(handler)
        elif args.make == 'seed':
            user_actions.make_seed(handler)
    elif args.run is not None:
        if args.run == 'normal':
            user_actions.run_normal(handler)
        elif args.run == 'seed':
            user_actions.run_seed(handler)
    elif args.host is not None:
        user_actions.update_server(handler)
    elif args.status is not None:
        status = user_actions.get_file_status(handler)
        print(f"Seed exists: {status['s']} | Normal exists: {status['n']} | Server name: {status['h']}")
    elif args.auto is not None:
        user_actions.run_auto_seed(handler)