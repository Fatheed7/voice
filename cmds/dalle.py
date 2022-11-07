import os
import openai
import urllib
import discord
from uuid import uuid4

queue = []
current = []

openai.api_key = os.getenv("OPENAI_API_KEY")


async def dalle_cmd(message):
    # msg = message.content
    # msg = msg.replace("!dalle ", "")
    queue.append(message)
    if current == []:
        current.append(message)
        await generate_image()


async def generate_image():
    current.append(queue[0])
    query = current[0].content.replace("!dalle ", "")
    try:
        generating = await current[0].channel.send(
            f'Generating Image for: {query}')
        response = openai.Image.create(
            prompt=query,
            n=2,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        urllib.request.urlretrieve(image_url, "image.png")
        file = discord.File("image.png", filename=str(uuid4) + ".png")
        await generating.delete()
        await current[0].channel.send(file=file)
        current.pop(0)
        queue.pop(0)
        if queue:
            await generate_image()
    except Exception as e:
        print(e)
        await generating.delete()
        await current[0].channel.send("Error: " + str(e))
