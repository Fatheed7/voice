from sound import SoundCommands
from moviepy.editor import concatenate_audioclips, AudioFileClip
import pyttsx3
import nextcord


async def duck_cmd(interaction, text, bot):
    channel = interaction.user.voice.channel
    voice = nextcord.utils.get(bot.voice_clients)
    vc = voice if voice and voice.is_connected() else (
        await channel.connect())
    if vc.is_playing():
        await interaction.send(
            "```\nHold on, I'm already playing a song dickhead.\n```")
        return
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.save_to_file(text, "duck/duck.mp3")
    engine.runAndWait()
    audio_clip_paths = [
        'duck/duck_p1.mp3',
        'duck/duck.mp3',
        'duck/duck_p2.mp3']
    clips = [AudioFileClip(p) for p in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    vol_down = final_clip.volumex(0.2)
    vol_down.write_audiofile('duck/duck_final.mp3')
    try:
        await SoundCommands.play(
            interaction, 'duck/duck_final.mp3', bot, 'duck/duck_final.mp3')
    except Exception as e:
        print(e)
