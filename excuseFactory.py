import openai
import json

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
    if location == "":
        return chatGPT(f"Create an excuse about why you can't attend your job as a tennis pro. You must address it in \"text message\" format to your boss, {pro}, and make sure to specficy the event happens at a random location you, the AI, create. The excuse doesn't have to involve tennis, but it can. My name is {name}.")
    return chatGPT(f"Create an excuse about why you can't attend your job as a tennis pro. You must address it in \"text message\" format to your boss, {pro}, and this event must take place in {location}. Keep it short, but include details. The excuse doesn't have to involve tennis, but it can. My name is {name}.")

print(generateExcuse(pro="Chris", location="", name="Trent"))