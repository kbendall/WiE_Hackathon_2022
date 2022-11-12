import os
import discord, json, random
from dotenv import load_dotenv
from quotes import *
from discord.utils import get

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


    #message responses
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
        
        #get a quote
        if user_message.lower() == '!quote':
            quote = getQuote()
            await message.channel.send(f'Hi {username}! Here is your quote!' + "\n" + "*" + str(quote) +"*")

        #warnings for people being sexist
        strikeOne = 1041080955072417893
        strikeTwo = 1041081117719150656
        strikeThree = 1041081171511091281
        standard = 1041099675027124256

        for i in flags['flags']:
            if i in message.content:
                if get(message.guild.roles, id=strikeOne) in message.author.roles:
                    await message.author.add_roles(get(message.guild.roles, id=strikeTwo))
                    await message.author.remove_roles(get(message.guild.roles, id=strikeOne))
                    await message.channel.send(f'Hey {username}! That message has been flagged as insensitive to gender minorities. If you think this is a mistake contact your sever admin. You now have the role {get(message.guild.roles, id=strikeTwo)}. On Strike THREE you will be auto banned.')
                elif get(message.guild.roles, id=strikeTwo) in message.author.roles:
                    await message.author.add_roles(get(message.guild.roles, id=strikeThree))
                    await message.author.remove_roles(get(message.guild.roles, id=strikeTwo))
                    await message.author.remove_roles(get(message.guild.roles, id=standard))
                    await message.channel.send(f'Hey {username}! That message has been flagged as insensitive to gender minorities. If you think this is a mistake contact your sever admin. You now have the role {get(message.guild.roles, id=strikeThree)}. You have been auto banned.')
                else:
                    await message.author.add_roles(get(message.guild.roles, id=strikeOne))
                    await message.channel.send(f'Hey {username}! That message has been flagged as insensitive to gender minorities. If you think this is a mistake contact your sever admin. You now have the role {get(message.guild.roles, id=strikeOne)}. On Strike THREE you will be auto banned.')
    
        #math question
        num = random.randint(0,2)
        if user_message.lower() == '!quiz-math':
            await message.channel.send(f"Hey {username}! Here's your question: ")
            await message.channel.send(data['math'][num]['q'])

            def check(m):
                return m.content == str(data['math'][num]['a']).lower()

            msg = await client.wait_for("message", check=check)
            await message.channel.send(f"Correct!")
        
        #programming quiz
        if user_message.lower() == '!quiz-programming':
            await message.channel.send(f"Hey {username}! Here's your question: ")
            await message.channel.send(data['programming'][num]['q'])

            def check(m):
                return m.content == str(data['programming'][num]['a']).lower()

            msg = await client.wait_for("message", check=check)
            await message.channel.send(f"Correct!")

        #fun facts quiz
        if user_message.lower() == '!quiz-fun-fact':
            await message.channel.send(f"Hey {username}! Here's your question: ")
            await message.channel.send(data['fun facts'][num]['q'])

            def check(m):
                return m.content == str(data['fun facts'][num]['a']).lower()

            msg = await client.wait_for("message", check=check)
            await message.channel.send(f"Correct!")

    client.run(TOKEN)


if __name__ == "__main__":
    main()