import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import getResponse, getAiResponse
from commands import getCommand

# load token
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# bot setup
intents = Intents.default()
intents.messages = True
intents.message_content = True
Client = Client(intents=intents)

# message funcitonnality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('User message is empty because intents were not enabled')
        return
    
    is_private = user_message[0] == "?"

    is_ai = user_message[0] == "$"

    is_command = user_message[0] == "!"

    if is_private or is_ai or is_command:
        user_message = user_message[1:]

    if is_command:
        result = await getCommand(message, user_message)
        await message.channel.send(result)
        return


    if is_ai:
        response : str = getAiResponse(user_message)
        await message.channel.send(response)
        return

    try:
        response : str = getResponse(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f'Error: {e}')

# startup

@Client.event
async def on_ready() -> None:
    print('Bot is ready')

# handle messages

@Client.event
async def on_message(message: Message) -> None:
    if message.author == Client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # log the user messages
    print(f'{username} in {channel} said: {user_message}')

    await send_message(message, user_message)

# run bot

def main() -> None:
    Client.run(TOKEN)

if __name__ == '__main__':
    main()