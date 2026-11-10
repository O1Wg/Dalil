import json
import random
from pathlib import Path

import discord 
from discord import app_commands
from discord.ext import commands

TIPS_FILE = Path(__file__).parent.parent / "tips.json"
TIPS = json.loads(TIPS_FILE.read_text(encoding="utf-8"))

class Tips(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

      @app_commands.command(name="tip", description="GEt a random study or coding tip")
      async def tip(self, interaction: discord.Interaction):
          all_tips = TIPS["study"] + TIPS["coding"]
          await interaction.responce.send_message(f" 💡 {random.choice(all_tips)}")

          async def setup(bot):
              await bot.add_cog(Tips(bot))
