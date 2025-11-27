import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
    
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$', intents=intents)

    async def on_ready(self):
        print(f"Bot is ready! Connected to : {self.user}")
        #ajouter des cogs
        pass

    async def on_member_join(self, member):
        guild = member.guild
        role = discord.utils.get(guild.roles, name="zgeg")
        if role:
            await member.add_roles(role)
            print(f"Rôle '{role.name}' attribué à {member.name}")

@commands.command()
async def test(ctx, arg):
    await ctx.channel.send(arg)

bot = MyBot()
bot.add_command(test)

bot.run('MTM4NTMwNDQyODAzODMyODMyMA.GP31em.GkfgNN_bxsl4KPyuJRwpk9rVLCyIeQJXr6zFpo')