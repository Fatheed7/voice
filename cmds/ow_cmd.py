import json

from sound import SoundCommands
from random import randrange


async def ow_cmd(interaction, client):  # sourcery skip: merge-comparisons
    char_list = ("ana", "ashe", "athena", "baptiste", "bastion", "brigitte",
                 "doomfist", "dva", "genji", "hanzo", "junkenstein",
                 "junkrat", "lucio", "mccree", "mei", "mercy", "moira",
                 "orisa", "pharah", "reaper", "reinhardt", "retribution",
                 "roadhog", "sigma", "soldier76", "sombra", "symmetra",
                 "torbjorn", "tracer", "training", "unused", "uprising",
                 "widowmaker", "winston", "wreckingball", "zarya", "zenyatta",
                 "kiriko", "junkerqueen", "sojourn")
    if interaction in char_list:
        sound_file = "overwatch/" + interaction + ".json"
    with open(sound_file, 'r') as j:
        data = json.loads(j.read())
        choice = randrange(len(data))
        sound = data[choice]
        path = "overwatch/" + interaction + "/" + sound['text']
        name = sound['text']
        try:
            await SoundCommands.play(interaction, path, client, name)
        except Exception as e:
            print(e)
