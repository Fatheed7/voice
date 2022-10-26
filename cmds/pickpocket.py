from sound import SoundCommands


async def pickpocket_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/Imperial/m/generic_pickpocket_00062274_1.mp3',
            client,
            'oblivion/Imperial/m/generic_pickpocket_00062274_1.mp3')
    except Exception as e:
        print(e)
