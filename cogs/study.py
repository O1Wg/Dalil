import discord
from discord import app_commands
from discord.ext import commands


class Study(commands.Cog):
    """Study commands: /tip and /duck."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Your commands go here, indented inside the class,
    # using @app_commands.command and self as the first parameter


async def setup(bot: commands.Bot):
    await bot.add_cog(Study(bot))
