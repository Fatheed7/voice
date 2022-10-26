import requests
import discord


async def temperature_cmd(message):
    users = {
        "Aria & Nick": {"Location": "Alblasserdam, NL", "Temperature": "0"},
        "Fatheed": {"Location": "Washington, GB", "Temperature": "0"},
        "Pickled": {"Location": "Gothenburg, SE", "Temperature": "0"},
        "James": {"Location": "Spring, Texas", "Temperature": "0"},
        "Kris": {"Location": "El Paso, Texas", "Temperature": "0"},
        }

    f_list = []
    c_list = []
    for value_ in users.values():
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" +
            value_['Location'] +
            "&units=imperial&APPID=af11f10d28833aac217eaee25199dda4")
        data = r.json()
        c_list.append(round((((data['main']['temp']) - 32) / 1.8), 1))
        f_list.append(round(data['main']['temp'], 1))

    embed = discord.Embed(
        title="By Azura! Here are the temperatures!",
        color=discord.Color.blue())

    embed.set_author(
        name="Adoring Weather Fan",
        icon_url="http://www.jasondunton.co.uk/fan.jpg")

    (embed.add_field(
        name="Milk Cult Member",
        value='\n'.join(f"{key}" for key in users),
        inline=True),)

    embed.add_field(
        name="Celsius",
        value='\n'.join(f"{v} °C" for v in c_list),
        inline=True)

    embed.add_field(
        name="Farhenheit",
        value='\n'.join(f"{v} °F" for v in f_list),
        inline=True)

    await message.channel.send(embed=embed)
