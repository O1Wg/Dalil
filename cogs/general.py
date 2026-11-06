import discord
from discord import app_commands
from discord.ext import commands


class General(commands.Cog):
    """Basic commands: /ping and /about."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(description="Check if Dalil is awake")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! {latency}ms")

    @app_commands.command(description="What is Dalil?")
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Dalil (دليل)",
            description="لكل رحلة دليل\nFrom your first line of code to your first job.",
            color=0x2B8A3E,
        )
        embed.set_footer(text="Built by a student, for students.")
        await interaction.response.send_message(embed=embed)
    @app_commands.command(description="Show Dalil's logo")
    async def logo(self, interaction: discord.Interaction):
      await interaction.response.send_message(discord_logo())


# discord.py calls this when bot.py loads the file
async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))

