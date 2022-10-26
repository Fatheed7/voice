import random
import json

from sound import SoundCommands
from random import randrange


async def npc_random_cmd(message, client):  # sourcery skip: merge-comparisons
    sound_files = ["json/argonian.json", "json/breton.json", "json/dark.json",
                   "json/dremora.json", "json/golden.json",
                   "json/highelf.json", "json/imperial.json",
                   "json/nord.json", "json/redguard.json",
                   "json/sheogorath.json", "json/skyrim.json"]
    choice = random.choice(sound_files)
    with open(choice, 'r') as j:
        sex = round(random.random())
        if (
            choice == 'json/breton.json'
                or choice == 'json/dremora.json'
                or choice == 'json/sheogorath.json'):
            data = json.loads(j.read())
            sound = random.choice(list(data['children'][0]['children']))
            path = sound['path']
            name = sound['name']
            try:
                await SoundCommands.play(message, path, client, name)
            except Exception as e:
                print(e)
        elif choice == 'json/skyrim.json':
            folder = randrange(104)
            data = json.loads(j.read())
            sound = random.choice(list(data['children'][folder]['children']))
            path = sound['path']
            name = sound['name']
            try:
                await SoundCommands.play(message, path, client, path)
            except Exception as e:
                print(e)
        else:
            data = json.loads(j.read())
            sound = random.choice(list(data['children'][sex]['children']))
            path = sound['path']
            name = sound['name']
            try:
                await SoundCommands.play(message, path, client, path)
            except Exception as e:
                print(e)
