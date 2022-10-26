from discord.ext import commands
import discord
from asyncio import sleep
from cmds import last
from pydub import AudioSegment
from collections import defaultdict
import re


class SoundCommands(commands.Cog):
    async def play(self, path, client, name):
        octaves = 0
        channel = self.author.voice.channel
        voice = discord.utils.get(client.voice_clients)
        pattern = "([a-zA-Z]=([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?)"  # noqa: W605 E501
        d = defaultdict(set)
        matches = re.finditer(pattern, self.content.lower(), re.MULTILINE)
        regex_list = [m.group(0) for m in matches]
        for r in regex_list:
            k, v = r.split("=")
            d[k].add(v)
        sound = AudioSegment.from_file(path, format="mp3")
        octaves = float(d["p"].pop()) if "p" in d else 0
        if octaves < -1 or octaves > 3:
            await self.channel.send(
                "```\nPitch must be between -1 and +3.```")
            return
        new_sample_rate = int(sound.frame_rate * (2.00 ** octaves))
        output_sound = sound._spawn(
            sound.raw_data, overrides={'frame_rate': new_sample_rate})
        output_sound = output_sound.set_frame_rate(44100)
        output_sound.export(
                "export/export.mp3", format="mp3")
        vc = voice if voice and voice.is_connected() else (
           await channel.connect())
        vc.play(discord.FFmpegPCMAudio("export/export.mp3"))
        await last.last_cmd("store", name, self)
        while vc.is_playing():
            await sleep(7200)
        await vc.disconnect()

    async def play_user(self, path, client, name):
        channel = self
        voice = discord.utils.get(client.voice_clients)
        vc = voice if voice and voice.is_connected() else (
            await channel.connect())
        vc.play(discord.FFmpegPCMAudio(path))
        await last.last_cmd("store", name, self)
        while vc.is_playing():
            await sleep(7200)
        await vc.disconnect()
