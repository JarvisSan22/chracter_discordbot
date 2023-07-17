import discord 
from discord import app_commands
from discord.ext import commands
#from discord_interactions import *
from dotenv import load_dotenv, find_dotenv
#from discord_slash import SlashCommand, SlashContext
import os
_ = load_dotenv(find_dotenv())

#bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
#slash_clinet=SlashCommand(bot,sync_commands=True)

class aclinet(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced =True 
        print("Bot has logged in")

client=aclinet()
tree=app_commands.CommandTree(client)

@tree.command(name="test",description="testing",guild=discord.Object(id=os.getenv("CHANNEL_ID")))
async def self(interaction: discord.Interaction, name:str):
    await interaction.response.send_message(f"hello ")

client.run(os.getenv("DISCORD_TOKEN"))