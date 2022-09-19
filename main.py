from ssl import Options
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

@rbot.slash_command(guild_ids=[1017094174316699769])        #Flips a coin
async def coinflip(ctx: discord.ApplicationContext):
    """Flips a coin."""
    c = ["HEADS!","TAILS!"]
    await ctx.respond("Flipping a coin!")
    await ctx.send(f"Result: {random.choice(c)}")

@rbot.slash_command(guild_ids=[1017094174316699769])        #Flips a coin
async def spin(ctx: discord.ApplicationContext,  number: discord.Option(str,name= "number", required=True)):
    """Spins a roulette."""
    await ctx.respond("Spinning the roulette!")
    await ctx.send(f"Result: {random.randint(1,int(number))}")



rbot.run(os.getenv('token'))