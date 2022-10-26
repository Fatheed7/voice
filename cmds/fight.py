from sound import SoundCommands


async def fight_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/high elf/m/generic_assaultnocrime_00062503_1.mp3',
            client,
            'oblivion/high elf/m/generic_assaultnocrime_00062503_1.mp3')
    except Exception as e:
        print(e)
