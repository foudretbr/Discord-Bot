import discord

class  MyClient(discord.client):
    async def on_ready(self):
        print(f'Logged on as {self.user} !')
    
    async def on_messsage(self, message):
        print(f'Message from {message.author} : {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('N1AWNcGY-RwSVvJQH8YR-hDM0DRdPiOU')


import discord
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
client.run('N1AWNcGY-RwSVvJQH8YR-hDM0DRdPiOU')
