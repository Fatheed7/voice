import os

import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from dotenv import load_dotenv

from cmds import (  # noqa: F401
    dalle_cmd, duck_cmd, gpt_cmd, itad_cmd, npc_specific, ow_cmd,
    randy_cmd, skyrim_cmd, npc_random)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = nextcord.Intents.all()
bot = commands.Bot()
servers = [721720706009661440, 867600394196484107]


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# Randy Command #
@bot.slash_command(guild_ids=servers,
                   description="All Hail Randy!")
async def randy(interaction: Interaction):
    await randy_cmd.randy_cmd(interaction)


# ITAD Command #
@bot.slash_command(guild_ids=servers,
                   description="Search for a game on Is There Any Deal?")
async def itad(
    interaction: Interaction,
    game: str = SlashOption(
        description="Enter the game you wish to search for.", required=True)):
    await itad_cmd.get_price(interaction, game)


# GPT Command #
@bot.slash_command(guild_ids=servers,
                   description="Generate a statement with GPT")
async def gpt(
    interaction: Interaction,
    text: str = SlashOption(
        description="Enter your statement", required=True, max_length=100)):
    await gpt_cmd.gpt_cmd(interaction, text)


# DALLE Command #
@bot.slash_command(guild_ids=servers,
                   description="Generate an image with DALL·E")
async def dalle(
    interaction: Interaction,
    text: str = SlashOption(
        description="Enter your statement", required=True, max_length=100)):
    await dalle_cmd.dalle_cmd(interaction, text)


# Duck Command #
@bot.slash_command(guild_ids=servers,
                   description="Add your text to Barbara Streisand\
                   by Duck Sauce")
async def duck(
    interaction: Interaction,
    text: str = SlashOption(
        description="Enter your text", required=True, max_length=100)):
    await duck_cmd.duck_cmd(interaction, text, bot)


# NPC Command #
@bot.slash_command(guild_ids=servers)
async def npc(interaction: nextcord.Interaction):
    pass


@npc.subcommand(description="Play a random Elder Scrolls sound.")
async def random(interaction: nextcord.Interaction):
    await npc_random.npc_random_cmd(interaction, bot)


@npc.subcommand(description="Play a random Skyrim sound.")
async def skyrim(interaction: nextcord.Interaction):
    await skyrim_cmd.skyrim_cmd(interaction, bot)


@npc.subcommand(description="Play a specific sound file.")
async def specific(
    interaction: nextcord.Interaction,
    text: str = SlashOption(
        description="Enter your statement",
        required=True,
        choices={
            "Arrow in the knee": "arrow",
            "Bed": "bed",
            "Bob": "bob",
            "Bread": "bread",
            "Cat": "cat",
            "Cheese": "cheese",
            "Curved Sword": "curved",
            "Fight!": "fight",
            "Here!": "here",
            "Here! Slow": "here2",
            "Honey sauce": "honey",
            "I don't know you": "knowyou",
            "Lemons": "lemons",
            "Necrophilia": "necro",
            "Nice": "nice",
            "Ni! Ni! Ni!": "ni",
            "PH": "ph",
            "Pickpocket!": "pp",
            "It's only smells": "smellz",
            "Snake!": "snake",
            "*snort*": "snort",
            "Stepbro": "stepbro",
            "It's a trap!": "trap",
            "Work! Work!": "work",
            "Wow!": "wow"
        })):
    await npc_specific.npc_path_cmd(interaction, bot, text)


# Overwatch Command #
@bot.slash_command(guild_ids=servers,
                   description="Play an Overwatch Sound File (Ana - Roadhog)")
async def ow(
    interaction: Interaction,
    text: str = SlashOption(
        description="Pick a Hero",
        required=True,
        choices={
            "Ana": "ana",
            "Ashe": "ashe",
            "Athena": "athena",
            "Baptiste": "baptiste",
            "Bastion": "bastion",
            "Brigitte": "brigitte",
            "Doomfist": "doomfist",
            "D.VA": "dva",
            "Genji": "genji",
            "Hanzo": "hanzo",
            "Junkenstein": "junkenstein",
            "Junker Queen": "junkerqueen",
            "Junkrat": "junkrat",
            "Kiriko": "kiriko",
            "Lúcio": "lucio",
            "McCree": "mccree",
            "Mei": "mei",
            "Mercy": "mercy",
            "Moira": "moira",
            "Orisa": "orisa",
            "Pharah": "pharah",
            "Reaper": "reaper",
            "Reinhardt": "reinhardt",
            "Retribution": "retribution",
            "Roadhog": "roadhog",
        })):
    await ow_cmd.ow_cmd(interaction, text, bot)


@bot.slash_command(guild_ids=servers,
                   description="Play an Overwatch Sound File\
                     (Sigma - Zenyatta)")
async def ow2(
    interaction: Interaction,
    text: str = SlashOption(
        description="Pick a Hero",
        required=True,
        choices={
            "Sigma": "sigma",
            "Soldier: 76": "soldier76",
            "Sombra": "sombra",
            "Sojourn": "sojourn",
            "Symmetra": "symmetra",
            "Torbjörn": "torbjorn",
            "Tracer": "tracer",
            "Training": "training",
            "Unused": "unused",
            "Uprising": "uprising",
            "Widowmaker": "widowmaker",
            "Winston": "winston",
            "Wrecking Ball": "wreckingball",
            "Zarya": "zarya",
            "Zenyatta": "zenyatta"
        })):
    await ow_cmd.ow_cmd(interaction, text, bot)


# Check user is in VC before attempting to join
@skyrim.before_invoke
@random.before_invoke
@specific.before_invoke
@duck.before_invoke
@ow.before_invoke
@ow2.before_invoke
async def ensure_voice(ctx):
    if ctx.user.voice is None:
        await ctx.send("You are not connected to a voice channel.")

bot.run(TOKEN)
