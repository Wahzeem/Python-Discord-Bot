# Imports
import os 
import discord
import aiohttp

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


### ---------- discord.Client ---------- ### 
# Represents a client connection that connects to Discord. 
# This class is used to interact with the Discord WebSocket and API.

# client = discord.Client(intents = intents)

### ---------- commands.Bot ---------- ### 
# Represents a Discord bot. 
# This is a sub class of 'discord.Client' and as a result 
# anything you can do with 'discord.Client' you can do with this bot.

bot = commands.Bot(command_prefix = "$", intents = intents)


# On start up
@bot.event
async def on_ready():
    print("Bot is running...")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(e)


### ---------- ($) commands ---------- ### 

# Greeting test
@bot.command(name = "hello")
async def greeting(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.channel.send(f"Greetings {username}!")

# Print test
@bot.command()
async def print(ctx, *args):
    response = ""
    if len(args):
        for arg in args:
            response = response + " " + arg
        await ctx.channel.send(response)
    return

# API request test
@bot.command(name = "dog")
async def dog_image(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
            data = await r.json()
            embed = discord.Embed(title = "Woof")
            embed.set_image(url = data['message'])
            await ctx.send(embed = embed)


### ---------- Forward slash commands ---------- ### 

@bot.tree.command(name="hello")
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command", ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction:discord.Interaction, thing_to_say:str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`")

@bot.tree.command(name="dog")
async def dog(interaction: discord.Interaction):
     async with aiohttp.ClientSession() as cs:
        async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
            data = await r.json()
            embed = discord.Embed(title = "Woof")
            embed.set_image(url = data['message'])
            await interaction.response.send_message(embed = embed)


# Run the bot
bot.run(os.environ.get('TOKEN'))