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

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205])        #Flips a coin
async def coinflip(ctx: discord.ApplicationContext):
    """Flips a coin."""
    c = ["HEADS!","TAILS!"]
    await ctx.respond("Flipping a coin!")
    await ctx.send(f"Result: {random.choice(c)}")

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205])        #Flips a coin
async def spin(ctx: discord.ApplicationContext,  number: discord.Option(str,name= "number", required=True)):
    """Spins a roulette."""
    await ctx.respond("Spinning the roulette!")
    await ctx.send(f"Result: {random.randint(1,int(number))}")

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205])        #Flips a coin
async def help(ctx: discord.ApplicationContext):
    """Displays information."""
    embed=discord.Embed(title="Random Bot",url="https://github.com/valentinoamato/Random-bot", description="Commands:",color=0xff5733)
    embed.add_field(name="/coinflip",value="Flips a coin.",inline=False)
    embed.add_field(name="/spin",value="Spins a roulette with the given amount of numbers.",inline=False)
    embed.add_field(name="/help",value="Displays information about the bot. ",inline=False)
    embed.add_field(name="/tf",value="Shows four random spanish cards to play a game called twenty four.\nBasically the idea of this game is to take the four numbers of the cards and make math operations between them to get to 24.\n\nE.g given the cards 12,6,5 and 2: (6-5)\*2\*12=24.",inline=False)
    await ctx.respond(embed=embed)


rbot.run(os.getenv('token'))