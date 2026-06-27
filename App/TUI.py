from time import sleep as s
import os
from colorim import Color
from Internals.ytdlp import yt_dwnld as ytd
from Internals.scraper import scrape
import sys



def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show_banner():
    banner = Color.hot_pink("""                                                 
▄▄▄▄  ▄▄▄  ▄▄▄▄                  ▄▄    ▄▄▄▄▄▄▄   
▀███  ███  ███▀       ██         ██    ███▀▀███▄ 
 ███  ███  ███  ▀▀█▄ ▀██▀▀ ▄████ ████▄ ███▄▄███▀ 
 ███▄▄███▄▄███ ▄█▀██  ██   ██    ██ ██ ███▀▀██▄  
  ▀████▀████▀  ▀█▄██  ██   ▀████ ██ ██ ███  ▀███ 
                                                 
                                                 v1.0""")   
    return banner

def main_menu():
    cls()
    print(Color.hot_pink("Welcome..."))
    s(1)
    print(Color.hot_pink("To..."))
    s(1)
    cls()
    print(show_banner())
    print()
    print()
    print(Color.hot_pink("1: Download Video from link."))
    print()
    print(Color.hot_pink("2: Download youtube video."))
    print()
    print(Color.hot_pink("Exit: Exits the TUI."))
    print()
    choice = input(Color.hot_pink("> "))
    if choice == "2":
        link = input(Color.hot_pink("> Link: "))
        if not link.startswith("https://"):
            link = f"https://{link}"
        ytd(link)
    
    if choice == "1":
        link = input(Color.hot_pink("> Link: "))
        scrape(link)
    if choice == "exit" or choice == "Exit":
        cls()
        print(Color.hot_pink("Goodbye!"))
        s(1)
        sys.exit()

main_menu()