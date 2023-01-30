# Imports
import os 
import discord
from discord.ext import commands
from dotenv import load_dotenv

import aiohttp
# import requests

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

# Greeting test
@bot.command(name = "hello")
async def greeting(ctx):
    username = str(ctx.author).split('#')[0]
    await ctx.channel.send(f"Greetings {username}!")

# Print test
@bot.command()
async def print(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.channel.send(response)

# API request test
@bot.command(name = "dog")
async def dog_image(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
            data = await r.json()
            embed = discord.Embed(title = "Woof")
            embed.set_image(url = data['message'])
            await ctx.send(embed = embed)

# Run the bot
bot.run(os.environ.get('TOKEN'))