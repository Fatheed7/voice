from sound import SoundCommands


async def arrow_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'skyrim/maleguard/dialogueguardsgeneral__00020954_1.wav',
            client,
            'skyrim/maleguard/dialogueguardsgeneral__00020954_1.wav')
    except Exception as e:
        print(e)
