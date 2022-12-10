import random
import json

from sound import SoundCommands
from random import randrange


async def skyrim_cmd(interaction, client):
    sound_files = "json/skyrim.json"
    with open(sound_files, 'r') as j:
        folder = randrange(104)
        data = json.loads(j.read())
        sound = random.choice(list(data['children'][folder]['children']))
        path = sound['path']
        try:
            await SoundCommands.play(interaction, path, client, path)
        except Exception as e:
            print(e)
