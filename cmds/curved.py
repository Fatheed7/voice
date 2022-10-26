from sound import SoundCommands


async def curved_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'skyrim/maleguard/dialogueguardsgeneral__000dd0db_1.wav',
            client,
            'skyrim/maleguard/dialogueguardsgeneral__000dd0db_1.wav')
    except Exception as e:
        print(e)
