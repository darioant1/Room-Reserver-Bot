import discord
from discord.ext import commands
from selenium_reserver import reserve_library_room  # import selenium_reserver reserve_library_room function

# set up intents (priveleges)
intents = discord.Intents.default()
intents.message_content = True  # allow bot to read messages

# bot token
TOKEN = 'your_token_here' # custom bot token from discord

client = discord.Client(intents=intents)  # passing intents

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!reserve'):
        email = '0'  # where the login info goes
        password = '0'
        PID = '0'
        groupName = '0'
        
        await message.channel.send('Reserving a room...')

        # call the function
        reserve_library_room(email, password, PID, groupName)

        await message.channel.send('Room reserved successfully!')

print(f"Bot token: {TOKEN}")  #  debugging for token
client.run(TOKEN)
