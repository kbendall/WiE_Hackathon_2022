import os
import discord
from dotenv import load_dotenv

def main():
    load_dotenv()
    TOKEN = 'MTA0MDk5NzU4OTE4Njc3MzAxMg.GtJT2Z.jPRbLHKXEzs_89MS_Vcgl0mRjg06xaVwdToKAk'

    client = discord.Client(intents=discord.Intents.default())
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!!!!!')

    @client.event
    async def on_message(message):
        print('HELLO')
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')
        if message.author == client.user:
            return
        await message.channel.send('hello')

        if message.channel.name == 'test':
            if user_message.lower() == 'hello':
                    return
    
    client.run(TOKEN)


if __name__ == "__main__":
    main()