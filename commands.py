from discord import Intents, Client, Message, VoiceChannel

async def getCommand(message : Message, user_message : str) -> str:
    user_message = user_message.lower()

    if user_message == "join":
        result = await join(message)
        return result
    
    if user_message == "leave":
        result = await leave(message)
        return result
    
    if user_message == "test":
        result = await test(message)
        return result
    
    return "Command not found"


async def join(message : Message) -> str:
    channel = message.author.voice.channel
    try:
        await channel.connect()
        return "Joined voice channel"
    except Exception as e:
        print(f'Error: {e}')
        return "Error joining voice channel"
    
async def leave(message : Message) -> str:
    channel = message.guild.voice_client
    try:
        await channel.disconnect()
        return "Left voice channel"
    except Exception as e:
        print(f'Error: {e}')
        return "Error leaving voice channel"
    
async def test(message : Message) -> str:
    channel = message.channel
    try:
        await channel.send("Test message")
        return "This is a the test message you have been waiting for" + message.author.mention + "!"
    except Exception as e:
        print(f'Error: {e}')
        return "Error sending test message"
