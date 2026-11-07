"""Shows "Playing Dalil" on your own Discord profile while you work.

This runs on your computer next to the Discord desktop app and is separate
from the bot. Start it in its own Git Bash window with:
    python tools/presence.py
Stop it with Ctrl+C.
"""

import os
import time

from dotenv import load_dotenv
from pypresence import Presence

load_dotenv()
CLIENT_ID = os.getenv("DISCORD_CLIENT_ID")

rpc = Presence(CLIENT_ID)
rpc.connect()

rpc.update(
    details="Building a Discord bot for students",
    state="Open source · every journey has a guide",
    large_image="dalil",  # the name you gave the image in Art Assets
    large_text="Dalil (دليل)",
    start=int(time.time()),  # shows how long you've been working
    buttons=[{"label": "View on GitHub", "url": "https://github.com/O1Wg/dalil"}],
)

print("Your profile now shows: Playing Dalil. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    rpc.close()
    print("Presence cleared.")
