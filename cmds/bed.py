from sound import SoundCommands


async def bed_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/Imperial/f/nqdanvil_greeting_0003e094_1.mp3',
            client,
            'oblivion/Imperial/f/nqdanvil_greeting_0003e094_1.mp3')
    except Exception as e:
        print(e)
