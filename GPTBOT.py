import openai
import os
from dotenv import load_dotenv, find_dotenv
from utils.voicevox_utils import speak
import urllib.parse as up
import requests
from datetime import datetime 
import panel as pn  # GUI
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')



class GalGPT:
    def __init__(self, system_settings, gal_id,temp=0):
        self.system={"role":"system","content":system_settings}
        self.input_list = [self.system]
        self.logs=[]
        self.model="gpt-3.5-turbo"
        self.temp=temp
    #Base chatGPT function
    def message_input(self,messages):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temp
        )
    #     print(str(response.choices[0].message))
        print(response)
        self.logs.append(response)
        self.input_list.append({"role":"assistant","content":response.choices[0].message.content})
   
