from sound import SoundCommands


async def snort_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/Imperial/m/generic_transition_0002a85b_1.mp3',
            client,
            'oblivion/Imperial/m/generic_transition_0002a85b_1.mp3')
    except Exception as e:
        print(e)
