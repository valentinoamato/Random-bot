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

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205,884926708355051581])        #Flips a coin
async def coinflip(ctx: discord.ApplicationContext):
    """Flips a coin."""
    c = ["HEADS!","TAILS!"]
    await ctx.respond("Flipping a coin!")
    await ctx.send(f"Result: {random.choice(c)}")

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205,884926708355051581])        #Flips a coin
async def spin(ctx: discord.ApplicationContext,  number: discord.Option(str,name= "number",description="Amount of numers of the roulette.",required=True)):
    """Spins a roulette."""
    await ctx.respond("Spinning the roulette!")
    await ctx.send(f"Numbers: {number}")
    await ctx.send(f"Result: {random.randint(1,int(number))}")

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205,884926708355051581])        #Flips a coin
async def help(ctx: discord.ApplicationContext):
    """Displays information."""
    embed=discord.Embed(title="Random Bot",url="https://github.com/valentinoamato/Random-bot", description="Commands:",color=0xff5733)
    embed.add_field(name="/coinflip",value="Flips a coin.",inline=False)
    embed.add_field(name="/spin",value="Spins a roulette with the given amount of numbers.",inline=False)
    embed.add_field(name="/help",value="Displays information about the bot. ",inline=False)
    embed.add_field(name="/24",value="Shows four random numbers to play a game called twenty four.\nBasically the idea of this game is to take the four numbers  and make math operations between them to get to 24.\n\nE.g given the numbers 12,6,5 and 2: (6-5)\*2\*12=24.",inline=False)
    await ctx.respond(embed=embed)

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="New Cards.",style=discord.ButtonStyle.blurple)
    async def menu1(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name=f"{random.randint(1,12)}                    {random.randint(1,12)}",value="----------------",inline=False)
        embed.add_field(name=f"{random.randint(1,12)}                    {random.randint(1,12)}",value="----------------",inline=False)
        await interaction.response.edit_message(embed=embed,content="This are your new cards:")

    @discord.ui.button(label="End Game.",style=discord.ButtonStyle.grey)
    async def menu2(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.random())
        embed.add_field(name="Thanks for Playing!!",value="\n<:wave:1024734969207205970><:wave:1024734969207205970><:wave:1024734969207205970>")
        await interaction.response.edit_message(embed=embed,content="Game Ended")
        self.value = False
        self.stop()

@rbot.slash_command(guild_ids=[1017094174316699769,1011807843164373092,965657683153793205,884926708355051581],name="24")
async def menu(ctx):
    """Shows four random spanish cards to play 24"""
    view = Menu()
    embed = discord.Embed(color=discord.Color.random())
    embed.add_field(name=f"{random.randint(1,12)}                    {random.randint(1,12)}",value="----------------",inline=False)
    embed.add_field(name=f"{random.randint(1,12)}                    {random.randint(1,12)}",value="----------------",inline=False)
    await ctx.respond("This are your cards:",view=view,embed=embed)

rbot.run(os.getenv('token'))