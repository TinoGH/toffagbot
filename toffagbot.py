import os
import discord
from Letters import Letters

TOKEN = os.environ['TOKEN']

robots = {}


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        global robots
        
        if message.content.startswith("toffagbot write"):
            if message.author not in robots.keys():
                await message.channel.send("Blup bloup... :/")
            else:
                text = robots[message.author].write(100)
                if len(text) > 0:
                    await message.channel.send(robots[message.author].write(100))
                else:
                    await message.channel.send("Blup bloup... :/")

        elif message.content.startswith("toffagbot learn"):
            async for message in message.channel.history(limit=10000):
                if message.author not in robots.keys():
                    robots[message.author] = Letters(6)
                robots[message.author].read(message.content + "\n")
            await message.channel.send("blip bloup blip... blipblip!")

        elif message.content.startswith("toffagbot"):
            await message.channel.send("Blop? Oo")

        else:
            if message.author not in robots.keys():
                robots[message.author] = Letters(6)
            robots[message.author].read(message.content + "\n")
                
                
client = MyClient()


client.run(TOKEN)
