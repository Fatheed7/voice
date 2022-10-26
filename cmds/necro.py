from sound import SoundCommands


async def necro_cmd(message, client):
    try:
        await SoundCommands.play(
            message,
            'oblivion/high elf/f/NQDSkingrad_SkingradTopic_00038AA1_3.mp3',
            client,
            'oblivion/high elf/f/NQDSkingrad_SkingradTopic_00038AA1_3.mp3')
    except Exception as e:
        print(e)
