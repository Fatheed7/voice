
from sound import SoundCommands
from dicts import elder, stupid


async def npc_path_cmd(
                        interaction,
                        bot,
                        text
                        ):  # sourcery skip: merge-comparisons
    if (text in elder.elderscrolls_dict):
        await SoundCommands.play(
            interaction, elder.elderscrolls_dict[text],
            bot, elder.elderscrolls_dict[text])
#  Check stupid_sound_dict for command.  #
    elif text in stupid.stupid_sound_dict:
        await SoundCommands.play(
            interaction, stupid.stupid_sound_dict[text],
            bot, stupid.stupid_sound_dict[text])
