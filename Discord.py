import discord 
from discord.ext import commands
from GPTBOT import GalGPT
from dotenv import load_dotenv, find_dotenv
import os
_ = load_dotenv(find_dotenv())

#bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
client=discord.Client(command_prefix="/", intents=discord.Intents.all())



async def greet():
    channel = client.get_channel(os.getenv("CHANNEL_ID"))
    print("Loaded")
    await channel.send('おはよう！')
@client.event
async def on_read():
    await greet

#class ChatButtons(discord.ui.view):
    #def __init__(self):
    #    super().__init__()
    #    self.add_item(discord.ui.Button(label="Gal info",url=""))

gal_dic={
    1906:{"name":"Kurumi Malenko","hair_color":"Mikan","Engery_source":"sunshine","character":"Wild and Pessimist","backstory":'This planet is covered in green, yellow, and purple plants - and the tall hills are covered in blue moss! no one even bats an eyelid. It looks inhabited here, but every person is asleep in their homes, in suspended animation. Do you dare wake them? The Goddess would want you to unravel this mystery. "Im the best!"'},
    273:{"name":"Amarilis Electron","hair_color":"Midnight","Engery_source":"sunshine","character":"Dark with a big EGO","backstory":'Your eyes open to see a spectacular view of the Milky Way. You think youll like it on your new home. The other Gals you met in the Brink are busy opening tea houses and spreading peace. But a villain is tearing this solar system to pieces and ruining peoples lives. Time to suit up and save this corner of the galaxy. "The wilds are calling me! You cant keep me locked up!"'},
    672:{"name":"Reylene Machina","hair_color":"Mizu","Engery_source":"Earth","character":"Stoic and Thoughtful","backstory":'Stop. Dont move. Youre landed in a dangerous place - take your time and take control. A youngster starts following you around. This is a strangely spiritual place. Things that wouldnt seem real happen regularly. You feel a rift in space and time here. And a whisper of a mission, given by the Goddess: guide the fallen to the next life. "Why is space used for trade? And for war as well! What a waste!"'}
}


def galtosstsyem(gal_info):
    system=f"""
    Your a cosmic gal from the galverse called {gal_info["name"]},
    You job is to reply to messages in a discord chat
    you have a {gal_info["character"]} personality,
    You have {gal_info["hair_color"]} colored hair, 
    your backstory is '''{gal_info["backstory"]}'''
    normaly reply in less than 200 words
    """
    return system




gal_api=GalGPT(galtosstsyem(gal_dic[1906]),1906)
# Discordでメッセージが送信されたときに呼び出される関数
@client.event
async def on_message(message):
    global gal_api
    # Bot自身が送信したメッセージには反応しない
    print(message)
    if message.author == client.user:
        return
    # ユーザーからの質問を受け取る
    if message.content.startswith('gal_gpt_launch'):    
        galid = message.content.replace("gal_gpt_launch","")
        print(galid)
        try:
            if int(galid) in gal_dic:
                galid=int(galid)
                print("Load gal ",gal_dic[galid]["name"])
                await message.channel.send(f"Load gal {gal_dic[galid]['name']}")
                gal_api=GalGPT(galtosstsyem(gal_dic[galid]),galid)
               
            else:
                #Gal not found 
                print("Gal not found, current gal ids ", list(gal_dic.keys))
                await message.channel.send(f"Gal not found, current gal ids {list(gal_dic.keys)}")
        except Exception as e:
            print(e)
            await message.channel.send("ERROR: gal load error", e)
    
    elif message.content.startswith("gal_gpt_chat"):
       
       try:
            # ChatGPTクラスを使って回答を生成する
            question = message.content.replace("gal_gpt_chat","")
            print("Question",question)
            print(len(gal_api.input_list))
            gal_api.input_list.append({"role":"user","content":question})
            gal_api.message_input(gal_api.input_list)
            # 生成した回答を取得する
            answer = gal_api.input_list[-1]["content"]
            print(answer)
            # 回答を送信する
            await message.channel.send(answer)
       except Exception as e:
          print("Error")
          await message.channel.send(f"Error {e}")
    

# Discord Botを起動する
client.run(token=os.getenv('DISCORD_TOKEN'))