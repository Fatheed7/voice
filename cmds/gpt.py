from transformers import pipeline


async def gpt_cmd(message):
    msg = message.content
    msg = msg.replace("!gpt ", "")
    print(msg)
    searching = await message.channel.send(
        f'Generating Text for: "{msg}" - (This may take upto 30 seconds!)')
    classifier = pipeline('text-generation', model='gpt2',
                          max_new_tokens=150)
    out = classifier(msg)
    await searching.edit(content="```txt\n" + out[0]['generated_text']
                         + "\n```")
