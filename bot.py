import os

import discord
from discord import app_commands
from dotenv import load_dotenv
from banner import show_banner, GREEN, GRAY, RESET

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = discord.Object(id=int(os.getenv("GUILD_ID")))


class Dalil(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Send the commands to the test server so they show up right away
        self.tree.copy_global_to(guild=GUILD)
        await self.tree.sync(guild=GUILD)


client = Dalil()


@client.event
async def on_ready():
    print(f"{GREEN}Online as {client.user}. Press Ctrl+C to stop.{RESET}")


@client.tree.command(description="Check if Dalil is awake")
async def ping(interaction: discord.Interaction):
    latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! {latency}ms")


@client.tree.command(description="What is Dalil?")
async def about(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Dalil (دليل)",
        description="لكل رحلة دليل\nFrom your first line of code to your first job.",
        color=0x2B8A3E,
    )
    embed.set_footer(text="Built by a student, for students.")
    await interaction.response.send_message(embed=embed)


# ... all your commands: /ping, /about, /tip ...


show_banner()
client.run(TOKEN)
print(f"{GRAY}Dalil is going to sleep. See you soon!{RESET}")
