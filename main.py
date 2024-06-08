import discord
from discord.ext import commands
from discord import Intents, Client, Message
from dotenv import load_dotenv
import os
import responses

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True 
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@client.event
async def on_message(message: Message) -> None:
    if message.author == Client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content[1:]
    channel: str = str(message.channel)

    if message.content.startswith('$$'):
        await ai_response(username, user_message, channel)
        return

    response = responses.getResponse(user_message)

    await message.channel.send(response)

async def ai_response(username, user_message, channel):
    response = "AI IS NOT WORKING YET"
    #send request to OPENAI

    #get response from OPENAI

    #send response to discord

    await channel.send(response)
    
# Run the bot
bot.run(TOKEN)
