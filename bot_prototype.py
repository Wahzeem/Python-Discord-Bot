import discord

TOKEN = "MTA2ODQwNDY3NjExNjA5OTA4Mg.Gixdvq.O-1BE8aE9UO5Qfo5qdJr9qVtN88H8roefzHHro"
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
