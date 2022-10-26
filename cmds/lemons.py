from sound import SoundCommands


async def lemons_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'skyrim/clown.mp3',
            client,
            'skyrim/clown.mp3')
    except Exception as e:
        print(e)
