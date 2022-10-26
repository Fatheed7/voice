from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
import discord


async def gamivo_cmd(message):
    msg = message.content
    searching = await message.channel.send(
        "Searching... (This may take a few seconds!)")
    options = Options()
    options.headless = False
    user_agent = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,'
        'like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    )
    options.add_argument("--window-size=1920,1200")
    options.add_argument('user-agent={0}'.format(user_agent))

    DRIVER_PATH = Service("gamivo/chromedriver.exe")

    driver = webdriver.Chrome(options=options, service=DRIVER_PATH)
    msg = msg.replace("!gamivo ", "")
    web_search = msg.replace(" ", "%20")
    URL = "https://www.gamivo.com/"
    driver.get(URL)
    search = driver.find_element(By.ID, "searchInputDesktop")
    sleep(2)
    search.send_keys(msg)
    sleep(1)
    search.send_keys(Keys.RETURN)
    sleep(5)
    from_class = driver.find_elements(By.XPATH, "//div[@class='from']//strong")
    title = driver.find_elements(By.CLASS_NAME, "product-card__details--title")
    link = driver.find_elements(By.CLASS_NAME, "product-card__view-offers")
    embed = discord.Embed(title=f"Gamivo Search for {msg.title()}",
                          color=discord.Color.blue())

    embed.set_author(
                name="Gamivo Search",
                icon_url=(
                    "https://skinlords.com/wp-content/uploads/"
                    "2021/08/gamivo-com-135x135.png"))
    if len(from_class) > 0:
        for i in range(len(from_class)):
            if i < 10:
                embed.add_field(name=title[i].text, value=(
                    (f'[from {from_class[i].text}]'
                     '(' + link[i].get_attribute('href')) + ')'), inline=False)

            else:
                embed.add_field(
                    name="More than 10 results were returned: ",
                    value='[View more on Gamivo]' +
                          '(https://www.gamivo.com/search/'
                    + web_search + ')', inline=True)
                break
        await searching.edit(content="", embed=embed)
    else:
        await message.channel.send(
            "Sorry daddy, there are no results for that game.")
    driver.quit()
