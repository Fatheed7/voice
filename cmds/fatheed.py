from sound import SoundCommands


async def fatheed_cmd(message, client):
    try:
        await SoundCommands.play_user(
            message,
            'stupid/nice.mp3',
            client,
            'stupid/nice.mp3')
    except Exception as e:
        print(e)
