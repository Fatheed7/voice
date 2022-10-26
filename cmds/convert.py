from urllib import request
import json
import discord


async def convert_cmd(message):  # sourcery skip: avoid-builtin-shadow
    msg = message.content.lower()
    type = msg.split(' ')[1]
    value = msg.split(' ')[2]
    from_type = msg.split(' ')[3]
    to_type = msg.split(' ')[4]
    from_split = from_type.split('=')[1]
    to_split = to_type.split('=')[1]
    value_split = value.split('=')[1]
    to_split = to_split.title()
    from_split = from_split.title()

    url = ('http://127.0.0.1:8000/convert/?' +
           type + "&" + value + "&" + from_type + "&" + to_type)
    print(url)

    req = request.Request(url)
    response = request.urlopen(req)
    result = json.loads(response.read().decode("utf-8"))

    print(result)

    if result['valid'] is True:
        await message.channel.send(result['result'])
    else:
        await message.channel.send('Error')

    embed = discord.Embed(
        title="By Azura! Here is your conversion!",
        color=discord.Color.blue())
    embed.set_author(
        name="Adoring Conversion Fan",
        icon_url="http://www.jasondunton.co.uk/fan.jpg")
    embed.add_field(name=from_split,
                    value=value_split, inline=True),
    embed.add_field(name="‎", value="‎"),
    embed.add_field(name=to_split,
                    value=result['result'], inline=True),
    await message.channel.send(embed=embed)
