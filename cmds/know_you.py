from sound import SoundCommands


async def know_you_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/breton/m/MS10_HELLO_0003C33F_1.mp3',
            client,
            'oblivion/breton/m/MS10_HELLO_0003C33F_1.mp3')
    except Exception as e:
        print(e)
