import os
import openai
import urllib
import nextcord
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

queue = []
current = []

openai.api_key = os.getenv("OPENAI_API_KEY")


async def dalle_cmd(interaction, message):
    print(openai.api_key)
    # msg = message.content
    # msg = msg.replace("!dalle ", "")
    queue.append(message)
    if current == []:
        current.append(message)
        await generate_image(interaction)


async def generate_image(interaction):
    current.append(queue[0])
    query = current[0]
    try:
        generating = await interaction.send(
            f'Generating Image for: {query}')
        response = openai.Image.create(
            prompt=query,
            n=2,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        urllib.request.urlretrieve(image_url, "image.png")
        file = nextcord.File("image.png", filename=str(uuid4) + ".png")
        await generating.delete()
        await interaction.send(file=file)
        current.pop(0)
        queue.pop(0)
        if queue:
            await generate_image()
    except Exception as e:
        print(e)
        await generating.delete()
        await interaction.send("Error: " + str(e))
