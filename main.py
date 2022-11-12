import os
import discord
from dotenv import load_dotenv
import json
from quotes import *

#@commands.command(pass_context = True)
def main():

    #loading json files
    load_dotenv()
    o = open('flagAsSexist.json')
    flags = json.load(o)
    o = open('questions.json')
    data = json.load(o)

    # setting up discord bot
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
                #addStrike(i, username)
    
        #math question
        if user_message.lower() == '!quiz':
            await message.channel.send(f"Hey {username}! Here's your question: ")
            await message.channel.send(data['question'][0]['q'])

            def check(m):
                print(m.content)
                return m.content == data['question'][0]['a']

            msg = await client.wait_for("message", check=check)
            await message.channel.send(f"Correct!")


    client.run(TOKEN)


if __name__ == "__main__":
    main()