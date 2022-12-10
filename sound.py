from nextcord.ext import commands
import nextcord
from asyncio import sleep


class SoundCommands(commands.Cog):
    async def play(self, path, client, name):
        channel = self.user.voice.channel
        voice = nextcord.utils.get(client.voice_clients)
        vc = voice if voice and voice.is_connected() else (
           await channel.connect())
        vc.play(nextcord.FFmpegPCMAudio(path))
        await self.send(
            "Playing " + name,
            ephemeral=True,
            delete_after=20)
        while vc.is_playing():
            await sleep(7200)
        await vc.disconnect()
