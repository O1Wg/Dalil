"""Shows "Playing Dalil" on your own Discord profile while you work.

This runs on your computer next to the Discord desktop app and is separate
from the bot. Start it in its own Git Bash window with:
    python tools/presence.py
Stop it with Ctrl+C.
"""

import os
import sys
import time

from pathlib import Path
from dotenv import load_dotenv
from pypresence import Presence

# dalil folder. That's where banner.py is.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pypresence.exceptions import DiscordNotFound
from banner import show_banner, GREEN, GRAY, RED, RESET # noqa: E402

load_dotenv()
CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")
if not CLIENT_ID:
    print(f"{RED}DISCORD_CLIENT_ID is missing from .env{RESET}")
    sys.exit(1)

show_banner()

rpc = Presence(CLIENT_ID)
try:
   rpc.connect()
except DiscordNotFound:
   print(f"{RED}Open the Discord desktop app first, then run this again.{RESET}")
   sys.exit(1)

rpc.update(
    details="Building a Discord bot for students",
    state="Open source · every journey has a guide",
    large_image="dalil",  # the name you gave the image in Art Assets
    large_text="Dalil (دليل)",
    start=int(time.time()),  # shows how long you've been working
    buttons=[{"label": "View on GitHub", "url": "https://github.com/O1Wg/dalil"}],
)

print(f"{GREEN}Your profile now shows: Playing Dalil. Press Ctrl+C to stop.{RESET}")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.close()
    print(f"{GRAY}Presence cleared. See you next time!{RESET}")
