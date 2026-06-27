import argparse
import sys
from colorim import Color
from TUI import cls
from Internals.scraper import scrape

if not len(sys.argv) == 2:
    print(Color.red("Pass in a link."))

link = sys.argv[1]

from Internals.ytdlp import yt_dwnld as ytd

parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", help="The mode for WatchR", required=True)
args = parser.parse_args()

modes = ["YouTube", "Youtube", "Website", "Other"]
if args.mode not in modes:

    print("That mode is not supported. try: ")
    cls()
    for item in modes:
        item = str(item)
        print(f"- {item}")
    sys.exit()
elif args.mode == "Youtube" or args.mode == "YouTube":
    ytd(link)
elif args.mode == "Website" or args.mode == "Other":
    scrape(link)