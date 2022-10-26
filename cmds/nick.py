from sound import SoundCommands


async def nick_cmd(message, client):
    try:
        await SoundCommands.play_user(
            message,
            'stupid/deerpenis.mp3',
            client,
            'stupid/deerpenis.mp3')
    except Exception as e:
        print(e)
