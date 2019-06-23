import discord
from Letters import Letters

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
                await message.channel.send("Sorry I don't know you :/")
            else:
                await message.channel.send(robots[message.author].write(100))
        elif message.content.startswith("toffagbot learn"):
            async for message in message.channel.history(limit=10000):
                if message.author not in robots.keys():
                    robots[message.author] = Letters(6)
                robots[message.author].read(message.content + "\n")
            await message.channel.send("blip bloup blip... blipblip!")
        else:
            if message.author not in robots.keys():
                robots[message.author] = Letters(6)
            robots[message.author].read(message.content + "\n")
                
                
client = MyClient()


def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client.run(token)
