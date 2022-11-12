import os
import discord
from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = 'MTA0MDk5NzU4OTE4Njc3MzAxMg.GtJT2Z.jPRbLHKXEzs_89MS_Vcgl0mRjg06xaVwdToKAk'

    client = discord.Client(intents=discord.Intents.all())
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!!!!!')
    
    @client.event
    async def on_message(message):

        #user information
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)

        #make sure we're not responding to bot messages
        if message.author == client.user:
             return

        #intro welcome message
        if user_message.lower() == 'wonderwoman':
            await message.channel.send(f'Hello {username}! Welcome to the Server:) I\'m WonderWoman, nice to meet you!')

    client.run(TOKEN)


if __name__ == "__main__":
    main()