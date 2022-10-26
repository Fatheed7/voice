import requests
import discord


async def owen_cmd(message):
    r = requests.get(
        "https://owen-wilson-wow-api.onrender.com/wows/random")
    data = r.json()

    embed = discord.Embed(
        title="Wow!",
        color=discord.Color.blue())

    embed.set_author(
        name="Adoring Owen Fan",
        icon_url=(
            "https://www.themoviedb.org/t/p/original/" +
            "op8sGD20k3EQZLR92XtaHoIbW0o.jpg"))

    embed.set_thumbnail(url=data[0]['poster'])

    (embed.add_field(
        name="Movie",
        value=data[0]['movie'],
        inline=True),)

    embed.add_field(
        name="Year",
        value=data[0]['year'],
        inline=True)

    embed.add_field(
        name="Timestamp",
        value=data[0]['timestamp'],
        inline=True)

    embed.add_field(
        name="Voice Line",
        value=data[0]['full_line'],
        inline=True)

    embed.add_field(
        name="Video",
        value="[Click me](" + str(data[0]['video']['1080p']) + ")",
        inline=True)

    embed.add_field(
        name="Audio",
        value="[Click me](" + str(data[0]['audio']) + ")",
        inline=True)

    await message.channel.send(embed=embed)
