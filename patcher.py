"""
Patches Squad to remove all the extra videos as it can break auto-mode.
"""
import winreg
import pathlib
import os
import vdf
from const import MOVIES


def patch_movies() -> bool:
    """
    Run the Squad movie patcher.
    """
    try:
        libraryfolders_config_location = get_steam_config_location()
        squad_install_location = get_squad_install_path(libraryfolders_config_location)
        squad_movies_location = get_squad_movie_path(squad_install_location)
        rename_movies(squad_movies_location)
        return True
    except OSError:
        print(OSError)

def get_steam_config_location() -> str:
    """
    Retrieves the steam base install location from registry.
    """
    registry_handle = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    steam_key = winreg.OpenKey(registry_handle,                      
                               r"SOFTWARE\WOW6432Node\Valve\Steam", 
                               0,
                               winreg.KEY_READ)
    install_path_key = winreg.QueryValueEx(steam_key, "InstallPath")[0]

    return pathlib.PurePath(install_path_key, "config", "libraryfolders.vdf")

def get_squad_install_path(library_folders: str) -> str:
    """
    Get the install location fro Squad from the libraryfolders.vdf file.
    """
    squad_install_path = ''
    with open(library_folders, 'r', encoding="UTF_8") as file:
        data = vdf.load(file)["libraryfolders"]
        for v_location in data:
            curr_v_location = data.get(v_location)
            for v_app in curr_v_location["apps"]:
                if v_app == "393380":
                    squad_install_path = curr_v_location["path"]
    return squad_install_path

def get_squad_movie_path(squad_steam_path:str) -> str:
    """
    Converts the Squad install directory to the Movies directory.
    """
    movie_path = pathlib.PurePath(squad_steam_path,
                                  "steamapps",
                                  "common",
                                  "Squad",
                                  "SquadGame",
                                  "Content",
                                  "Movies"
                                  )
    return movie_path

def get_filenames_without_extension(filenames: object) -> object:
    """
    Removes the file extension from a list of file names.
    """
    return [file.split(".")[0] for file in filenames]

def patch_file(filename: str, path: str) -> bool:
    """
    Patches a file to be unreferenceable by Squad.
    """
    try:
        patched_filename = "zzz_"  + filename + ".mp4"
        filename = filename + ".mp4"
        os.rename(path / filename , path / patched_filename)
        print(f"File patched from: {filename} to: {patched_filename}.")
        return True
    except OSError:
        print(OSError)


def rename_movies(path_to_movies: str) -> None:
    """
    Renames files in the Movies directory that affect startup.
    """
    dir_contents = get_filenames_without_extension(os.listdir(path_to_movies))
    for full_filename in dir_contents:
        patched = False
        if full_filename in MOVIES and ("zzz_" + full_filename) not in dir_contents:
            patched = patch_file(full_filename, path_to_movies)
        elif "zzz" in full_filename and full_filename in dir_contents:
            print(f"Patched file {full_filename} already exists.")
        elif full_filename in dir_contents and "zzz_" + full_filename in dir_contents:
            print(f"Patched file {full_filename} and unpatched file co-exist.")
            try:
                file_to_remove = "zzz_" + full_filename + ".mp4"
                os.remove(path_to_movies / file_to_remove)
                print(f"Removed zzz_{full_filename}")
                patched = patch_file(full_filename, path_to_movies)
            except OSError:
                print(OSError)
        else:
            print(f"Unpatchable file {full_filename} exists.")
        if patched:
            dir_contents = get_filenames_without_extension(os.listdir(path_to_movies))
