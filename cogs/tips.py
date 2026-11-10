import json
import random
from pathlib import Path

import discord
from discord import app_commands
from discord.ext import commands

TIPS = json.loads((Path(__file__).parent.parent / "tips.json").read_text(encoding="utf-8"))


class Tips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="tip", description="Get a random study or coding tip")
    async def tip(self, interaction: discord.Interaction):
        text = random.choice(TIPS["study"] + TIPS["coding"])
        await interaction.response.send_message(f"💡 {text}")


async def setup(bot):
    await bot.add_cog(Tips(bot))
