async def last_cmd(action, path, message):
    if action == "store":
        file = open("last/last.txt", "w")
        file.write(path)
        file.close()
    elif action == "read":
        f = open("last/last.txt", "r")
        try:
            if f.mode == 'r':
                contents = f.read()
                await message.channel.send(
                    'The last file played was: ' + contents)
        except UnboundLocalError:
            await message.channel.send('No sound file has been played yet.')
