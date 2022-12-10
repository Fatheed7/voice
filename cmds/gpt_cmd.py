from transformers import pipeline


async def gpt_cmd(interaction, arg):
    print(arg)
    searching = await interaction.send(
        f'Generating Text for: "{arg}" - (This may take upto 30 seconds!)')
    classifier = pipeline('text-generation', model='gpt2',
                          max_new_tokens=150)
    out = classifier(arg)
    await searching.edit(content="```txt\n" + out[0]['generated_text']
                         + "\n```")
