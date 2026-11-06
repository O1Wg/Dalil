import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

from banner import show_banner, GREEN, GRAY, RESET

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = discord.Object(id=int(os.getenv("GUILD_ID")))

COGS_DIR = Path(__file__).parent / "cogs"


class Dalil(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned,  # Dalil only uses slash commands
            help_command=None,
            intents=discord.Intents.default(),
        )

    async def setup_hook(self):
        # Load every file in cogs/ (each file is one group of commands)
        for file in sorted(COGS_DIR.glob("*.py")):
            if not file.name.startswith("_"):
                await self.load_extension(f"cogs.{file.stem}")

        # Send the commands to the test server so they show up right away
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)


bot = Dalil()


@bot.event
async def on_ready():
    print(f"{GREEN}Online as {bot.user}. Press Ctrl+C to stop.{RESET}")


show_banner()
bot.run(TOKEN)
print(f"{GRAY}Dalil is going to sleep. See you soon!{RESET}")
