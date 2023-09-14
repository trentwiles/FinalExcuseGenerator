import openai
import json
import random

def chatGPT(message):
    openai.api_key = json.loads(open("config.json").read())["key"]

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )

    return completion.choices[0].message["content"]

def generateExcuse(pro, location, name):
    print(pro + "" + location + name)
    if location == "":
        return chatGPT(f"Write a text message to my boss, {pro}, about why I can't come to my job as a tennis pro. Make sure to specficy the event happens at a random location you, the AI, create. The excuse doesn't have to involve tennis, but it can. My name is {name}. Keep it brief.")
    return chatGPT(f"Write a text message to my boss, {pro}, about why I can't come to my job as a tennis pro. Make sure to specficy the excuse take place at {location}, the AI, create. The excuse doesn't have to involve tennis, but it can. My name is {name}. Keep it brief.")

def messageFromBoss():
    messages = ["hey fellas, i need u on trash 2day thx!", "hey fellas I need a jr pro on red ball today", "morning I need a jr pro to come in and dry the courts"]
    return messages[random.randint(0,len(messages))]
#print(generateExcuse(pro="Chris", location="", name="Trent"))