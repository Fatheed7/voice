from sound import SoundCommands


async def ni_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/argonian/f/senqdmania_serunsincirclesyell_'
            '00041211_1.mp3',
            client,
            'oblivion/argonian/f/senqdmania_serunsincirclesyell_'
            '00041211_1.mp3',)
    except Exception as e:
        print(e)
