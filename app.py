import os

import discord
from dotenv import load_dotenv
import discord.ext
from sound import SoundCommands

from cmds import (  # noqa: F401
    embed, last, nick, play_sound,
    itad, gamivo, gpt, duck, temperature,
    convert, skyrim, npc_random, fatheed,
    owen, dalle
    )

from dicts import cmd_dict, elder, stupid

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(self):
    if self.content.lower().startswith("!npc "):
        string = self.content.lower().split(" ", 1)[1]
    else:
        string = self.content.lower()
    #  ITAD API Command  #
    if self.content.lower().startswith('!price '):
        await itad.get_price(self)
    elif self.content.lower().startswith('!owen'):
        await owen.owen_cmd(self)
    #  Gamivo Command  #
    # elif self.content.lower().startswith('!gamivo '):
    #    await gamivo.gamivo_cmd(self)
    #  GPT Command  #
    elif self.content.lower().startswith('!gpt '):
        await gpt.gpt_cmd(self)
    elif self.content.lower().startswith('!dalle '):
        await dalle.dalle_cmd(self)
    #  Check if user is in a voice channel.  #
    elif self.author.voice is None and self.content.startswith("!npc"):
        await self.channel.send('You are not in a voice channel.')
    #  Check sound_dict for command.  #
    elif (self.content.startswith("!npc") and
            string in elder.elderscrolls_dict):
        await SoundCommands.play(
            self, elder.elderscrolls_dict[string],
            client, elder.elderscrolls_dict[string])
    #  Check stupid_sound_dict for command.  #
    elif (self.content.startswith("!npc") and
            string in stupid.stupid_sound_dict):
        await SoundCommands.play(
            self, stupid.stupid_sound_dict[string],
            client, stupid.stupid_sound_dict[string])
    #  Check cmd_dict for command.  #
    elif string in cmd_dict.cmd_dict:
        await eval(cmd_dict.cmd_dict[string])
    #  Stupid Duck Command.  #
    elif self.content.lower().startswith('!duck '):
        await duck.duck_cmd(self, client)
    elif self.content.lower().startswith('!convert'):
        await convert.convert_cmd(self)
    #  Play sound file with path  #
    elif self.content.lower().startswith("!npc "):
        await play_sound.play_sound_cmd(self, client)


# @client.event
# async def on_voice_state_update(member, before, after):
#     if ((not before.channel and after.channel and
#          str(member)) == "Fatheed#9994"):
#         await sleep(3)
#         await fatheed.fatheed_cmd(after.channel, client)

client.run(TOKEN)
