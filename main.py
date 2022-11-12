import os
import discord
from dotenv import load_dotenv
import json
from quotes import *

@commands.command(pass_context = True)
def main():
    load_dotenv()
    o = open('flagAsSexist.json')
    flags = json.load(o)
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
        
        if user_message.lower() == '!quote':
            quote = getQuote()
            await message.channel.send(f'Hi {username}! Here is your quote!' + "\n" + "*" + str(quote) +"*")


        for i in flags['flags']:
            if message.content == i:
                await message.channel.send(f'Hey {username}! That message has been flagged as insensitive to gender minorities. If you think this is a mistake contact your sever admin. This is your {username} strike before auto-ban.')
                addStrike(i, username)
    
        #math question
        if user_message.lower() == '!quiz':
            await message.channel.send(f"Hey {username}! Here's your question: ")
            await message.channel.send(f"What is 1 + 1?" )
        
            def check(m):
                return m.content == "2"

            msg = await client.wait_for("message", check=check)
            if message.content == '2':
                await message.channel.send("Nice")
                await message.channel.send(f"Hello {msg.author}!")

            # msg = client.wait_for("message", check=check)
            # await message.channel.send(f"Correct {username}!")
            # msg = await client.wait_for("message", check=check)
            # await message.channel.send(f"Correct {msg.author}!")

    client.run(TOKEN)


if __name__ == "__main__":
    main()