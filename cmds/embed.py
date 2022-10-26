import discord


async def embed_cmd(ctx):
    embed = discord.Embed(
        title="By Azura! Here are the bot commands!",
        color=discord.Color.blue())
    embed.set_author(
        name="Adoring Fan",
        icon_url="http://www.jasondunton.co.uk/fan.jpg")
    embed.add_field(name="Commands",
                    value="‎"
                    "!npc\n"
                    "!npc bed\n"
                    "!npc cheese\n"
                    "!npc knowyou\n"
                    "!npc last\n"
                    "!npc necro\n"
                    "!npc ni\n"
                    "!npc random\n"
                    "!npc pp\n"
                    "!npc snort\n"
                    "!npc skyrim", inline=True),
    embed.add_field(name="‎", value="‎"),
    embed.add_field(name="Response", value="‎"
                    "Shows this embed!\n"  # !npc
                    "Heh, Seamen\n"  # !npc bed
                    "Cheese for everyone!\n"  # !npc cheese
                    "I don't know you and "  # !npc knowyou
                    "I don't care to know you.\n"  # !npc knowyou
                    "Shows the last sound clip played.\n"  # !npc last
                    "Necrophilia?\n"  # !npc necro
                    "Ni! Ni! Ni! Ni! Ni!\n"  # !npc ni
                    "Plays a random sound file.\n"  # !npc
                    "Pickpocket! Pickpocket!\n"  # !npc pp
                    "*snorts*\n"  # !npc snort
                    "Plays a random Skyrim sound",  # !npc skyrim
                    inline=True)
    await ctx.send(embed=embed)
