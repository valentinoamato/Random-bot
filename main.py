import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True



rbot = commands.Bot(intents=intents)
@rbot.event
async def on_ready():
    print(f'We have logged in as {rbot.user}')




@rbot.event
async def on_message(message):
    if message.author == rbot.user:
        return
    
    if message.content == '$hello':
        await message.channel.send('hello!!!')

rbot.run(os.getenv('token'))