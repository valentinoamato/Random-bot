import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random

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

@rbot.slash_command()        #Flips a coin
async def coinflip(ctx: discord.ApplicationContext,guild_ids=[965657683153793205]):
    """Flips a coin."""
    c = ["HEADS!","TAILS!"]
    await ctx.send(random.choice(c))

rbot.run(os.getenv('token'))