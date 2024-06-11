from random import randint
from discord import Intents, Client, Message, VoiceChannel

# messages the bot can send
join_message = ["Just joined, what's up?", "I'm here now, what's going on?", "I've arrived, what's the plan?", "I'm here, what's up?", "I've joined, what's happening?", "I'm here now, what's up?", "I'm here, what's going on?", "I've arrived, what's going on?", "I've joined, what's up?", "I'm here, what's the plan?", "Good morning vietnam!", "Yellow, I am here", "Wassup!", "Give me a sec..."]
leave_message = ["I'm out, see ya!", "I'm leaving, goodbye!", "I'm out, goodbye!", "I'm leaving, see ya!", "I'm out, goodbye!", "I'm leaving, see ya!", "I'm out, see ya!", "I'm leaving, goodbye!", "I'm out, goodbye!", "I'm leaving, see ya", "buh bye!", "See ya broosky", "I'm out, peace!", "I'm out, peace!", "I'm out, peace!", "I'm out, peace!"]
command_not_found_message = ["WDYM, I don't get it :(", "I don't understand :(", "Can you repeat that :(", "I'm not sure what you mean :(", "I don't know what you mean :(", "I don't understand :(", "I'm not sure what you mean :(", "I don't understand :(", "Bro speak more clearly :(", "You need to learn to type :(", "I think you made a typo :(" ]

# list of commands
command_list = ["join", "leave", "test", "help"]

# add say command

# add play command

# add yell command

# add whisper command

# add spam command

# add tag mechanism

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
    
    if user_message == "help":
        result = await help(message)
        return result
    
    return command_not_found_message[randint(0, len(command_not_found_message) - 1)]


async def join(message : Message) -> str:
    try:
        channel = message.author.voice.channel
        await channel.connect()
        return join_message[randint(0, len(join_message) - 1)]
    except Exception as e:
        print(f'Error: {e}')
        return "Error joining voice channel :("
    
async def leave(message : Message) -> str:
    try:
        channel = message.guild.voice_client
        await channel.disconnect()
        return leave_message[randint(0, len(leave_message) - 1)]
    except Exception as e:
        print(f'Error: {e}')
        return "Error leaving voice channel :("
    
async def test(message : Message) -> str:
    try:
        channel = message.channel
        await channel.send("Hold on, I'm sending a test message...")
        return "This is a the test message you have been waiting for" + message.author.mention + "!!!"
    except Exception as e:
        print(f'Error: {e}')
        return "Error sending test message :("
    
async def help(message : Message) -> str:
    try:
        channel = message.channel
        commands = ", ".join(command_list)
        await channel.send("To use commands, type ! followed by the command name. \nFor example, to join a voice channel, type !join. \nHere is a list of commands: " + commands + ". \nTo talk to my AI, type $ followed by your message. \nTo send me a private message, type ? followed by your message. \nTo get a private message from me, use ? followed by your message.")
        return "Here you go!"
    except Exception as e:
        print(f'Error: {e}')
        return "Error sending help message :("
