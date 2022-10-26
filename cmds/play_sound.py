from sound import SoundCommands
import re


async def play_sound_cmd(message, client):
    sound = (re.sub(r'.', '', message.content, count=5))
    try:
        await SoundCommands.play(
            message,
            sound,
            client,
            sound)
    except Exception as e:
        print(e)
        await message.channel.send(
            "```\nSorry daddy, I can't find that sound file\n```")
