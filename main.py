import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'MTA0MDk5NzU4OTE4Njc3MzAxMg.GtJT2Z.jPRbLHKXEzs_89MS_Vcgl0mRjg06xaVwdToKAk'

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!!!!!')

client.run(TOKEN)