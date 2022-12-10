import requests
import os
import nextcord


from dotenv import load_dotenv
load_dotenv()
KEY = os.getenv('ITAD_KEY')


async def get_price(interaction, game):
    # sourcery skip: remove-redundant-pass, use-fstring-for-concatenation
    plain_response = requests.get(
        "https://api.isthereanydeal.com/v02/game/plain/?key="
        + KEY + "&title=" + game + "&region=eu2")
    print(plain_response.json())
    plain = plain_response.json()['data']['plain']
    response = requests.get(
        "https://api.isthereanydeal.com/v01/game/prices/?key="
        + KEY + "&plains=" + plain + "&region=eu2")
    embed = nextcord.Embed(
        title="Are there any deals for " + game + "?",
        color=nextcord.Color.blue())
    embed.set_author(
            name="Is There Any Deal",
            icon_url=(
                "https://pbs.twimg.com/profile_images/"
                "1169691692892655619/TbXBDxfj_400x400.jpg"))
    items = response.json()['data'][plain]['list']
    if len(items) > 0:
        for item in response.json()['data'][plain]['list']:
            embed.add_field(name=item['shop']['name'],
                            value='[€' + f"{(item['price_new']):.2f}" +
                            '](' + item['url'] + ')',
                            inline=True)
        await interaction.send(embed=embed)
    else:
        await interaction.send(
            "Sorry daddy, there are no results for that game.")
