import discord

class Bot(discord.Client):

    def __init__ (self):
        super().__init__()


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

    async def on_message(self,message):
        if(message.author == self.user):
            return
        if(message.content.startswith("!apero")):
            await message.channel.send("Aaaaaapero")

if __name__ == "__main__":
    bot = Bot()
    bot.run("NzEyNjUyNzE2MjE1NzYyOTY1.XsUrmw.vNCiHBBBXVIvQyNyeIgioPTp560")
