from sound import SoundCommands


async def cheese_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/sheogorath/m/se04shell_se04xedilianchoice_'
            '00044f52_1.mp3',
            client,
            'oblivion/sheogorath/m/se04shell_se04xedilianchoice_'
            '00044f52_1.mp3',)
    except Exception as e:
        print(e)
