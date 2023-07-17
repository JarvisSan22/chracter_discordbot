
import discord 
from discord.ext import commands
from GPTBOT import GalGPT
from dotenv import load_dotenv, find_dotenv
import os
_ = load_dotenv(find_dotenv())
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

gal_dic={
    1906:{"name":"Kurumi Malenko","hair_color":"Mikan","Engery_source":"sunshine","character":"Wild and Pessimist","backstory":'This planet is covered in green, yellow, and purple plants - and the tall hills are covered in blue moss! no one even bats an eyelid. It looks inhabited here, but every person is asleep in their homes, in suspended animation. Do you dare wake them? The Goddess would want you to unravel this mystery. "Im the best!"'},
    273:{"name":"Amarilis Electron","hair_color":"Midnight","Engery_source":"sunshine","character":"Dark with a big EGO","backstory":'Your eyes open to see a spectacular view of the Milky Way. You think youll like it on your new home. The other Gals you met in the Brink are busy opening tea houses and spreading peace. But a villain is tearing this solar system to pieces and ruining peoples lives. Time to suit up and save this corner of the galaxy. "The wilds are calling me! You cant keep me locked up!"'},
    672:{"name":"Reylene Machina","hair_color":"Mizu","Engery_source":"Earth","character":"Stoic and Thoughtful","backstory":'Stop. Dont move. Youre landed in a dangerous place - take your time and take control. A youngster starts following you around. This is a strangely spiritual place. Things that wouldnt seem real happen regularly. You feel a rift in space and time here. And a whisper of a mission, given by the Goddess: guide the fallen to the next life. "Why is space used for trade? And for war as well! What a waste!"'}
}

#Drop down
class GalDropDown(discord.ui.Select):
    def __init__(self):
        option=[discord.SelectOption(label=gal_dic[id]["name"],description=gal_dic[id]["character"]) for id in list(gal_dic.keys())]
        super().__init__(placeholder="Gal options",options=option,min_values=1,max_values=1)
    
    async def callback(self, interaction: discord.Interaction):
        print(self.values)
        await interaction.message.delete()
        await interaction.channel.send(f"You chose of gal '{self.values[0]}'")

class GalView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(GalDropDown())

@bot.command()
async def gal(ctx: commands.Context):
    await ctx.send("Click drop down to select gal",view=GalView())

bot.run(token=os.getenv('DISCORD_TOKEN'))
