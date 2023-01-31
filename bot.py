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
    url = "https://dog.ceo/api/breeds/image/random"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            data = await r.json()
            embed = discord.Embed(title = "Woof")
            embed.set_image(url = data['message'])
            await interaction.response.send_message(embed = embed)

@bot.tree.command(name="steam_search")
@app_commands.describe(key_word = "What to search?")
async def steam_search(interaction:discord.Interaction, key_word:str):
    url = f"https://steam2.p.rapidapi.com/search/{key_word}/page/1"
    headers = {
	"X-RapidAPI-Key": "66d7718980msh3825a3ff4926de5p16af01jsna73efc092cc8",
	"X-RapidAPI-Host": "steam2.p.rapidapi.com"
    }
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url, headers = headers) as r:
            data = await r.json()
            await interaction.response.send_message(str(data[0]['url']))


# Run the bot
bot.run(os.environ.get('TOKEN'))