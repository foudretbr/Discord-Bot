import discord
from discord.ext import commands
from discord.ext import context
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX', '$')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
    
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, intents=intents)

    async def on_ready(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

        print(f"Bot is ready! Connected to : {self.user}")

    async def on_member_join(self, member):
        guild = member.guild
        role = discord.utils.get(guild.roles, name="zgeg")
        if role:
            await member.add_roles(role)
            print(f"Rôle '{role.name}' attribué à {member.name}")

    async def on_message(self, message):
        if not message.author.bot:
            if "nigger" in message.content.lower():
                # await message.delete()
                await message.channel.send(f'{message.author.mention}, NIGGER !')

        await self.process_commands(message)

# @commands.command()
# async def test(ctx, arg):
#     await ctx.channel.send(arg)

# @commands.command()
# async def channel(ctx):
#     i = 1
#     for channel in ctx.guild.channels:
#         await ctx.send(f'{i} : {channel.name}')
#         i += 1

# @commands.command()
# async def clear(ctx):
#     await ctx.channel.purge(limit=100)

bot = MyBot()
# bot.add_command(test)
# bot.add_command(clear)
# bot.add_command(channel)

bot.run(TOKEN)