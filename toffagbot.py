import os
import discord
from Letters import Letters

TOKEN = os.environ['TOKEN']


class MyClient(discord.Client):

    def __init__(self):
        discord.Client.__init__(self)
        self.robots = {}

    def read(self, author, text):
        if author not in self.robots.keys():
            self.robots[author] = Letters(6)
        self.robots[author].read(text + "\n")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith("toffagbot write"):
            if message.author not in self.robots.keys():
                await message.channel.send("Blup bloup... :/")
            else:
                text = self.robots[message.author].write(100)
                if len(text) > 0:
                    await message.channel.send(text)
                else:
                    await message.channel.send("Blup bloup... :/")

        elif message.content.startswith("toffagbot learn"):
            async for message in message.channel.history(limit=10000):
                self.read(message.author, message.content)
            await message.channel.send("blip bloup blip... blipblip!")

        elif message.content.startswith("toffagbot"):
            await message.channel.send("Blop? Oo")

        else:
            self.read(message.author, message.content)
                
                
client = MyClient()


client.run(TOKEN)
