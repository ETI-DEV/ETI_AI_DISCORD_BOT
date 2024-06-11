from random import randint
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_KEY)

helloResponses = ["Sup", "Yo", "My man!", "Yellow!", "Waddup", "Hey", "Hello", "Hi", "Greetings", "Salutations", "Howdy", "Hey there", "Hey you", "Hey buddy", "Hey friend", "Hey pal"]
goodbyeResponses = ["Goodbye", "Bye", "See ya", "Later", "Farewell", "Adios", "Cya", "Catch ya later", "Peace out", "Take care", "Goodnight", "Goodbye!", "Goodbye.", "Goodbye!", "Go away", "Bu bye"]
message_found_message = ["WDYM, I don't get it :(", "I don't understand :(", "Can you repeat that :(", "I'm not sure what you mean :(", "I don't know what you mean :(", "I don't understand :(", "I'm not sure what you mean :(", "I don't understand :(", "Bro speak more clearly :(", "You need to learn to type :(", "I think you made a typo :(" ]

def getResponse(user_input : str) -> str:
    lowered = user_input.lower()
    
    # hello responses
    if lowered in [response.lower() for response in helloResponses]:
        return helloResponses[randint(0, len(helloResponses) - 1)]
    
    # goodbye responses
    if lowered in [response.lower() for response in goodbyeResponses]:
        return goodbyeResponses[randint(0, len(goodbyeResponses) - 1)]
    
    # if no response is found
    return message_found_message[randint(0, len(message_found_message) - 1)]

def getAiResponse(user_input : str) -> str:
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            temperature=1,
            max_tokens=200,
            top_p=0.8,
            frequency_penalty=0,
            presence_penalty=0
            )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f'Error: {e}')
        return "Sorry, I'm having trouble understanding you right now."