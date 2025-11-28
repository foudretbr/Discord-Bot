import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import context

class Moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(name="kick", description="Kick an user out of the serve.")
    @commands.has_permissions(kick_members=True)
    @app_commands.describe(user="The user to kick", reason="The reason why the user should be kick")
    async def kick(self, context: context, user: discord.User, *, reason: str = "Not specified"):
        """Kick an user from the server """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(user.id)
        if member.guild_permissions.administrator:
            embed = discord.Embed(description="User has administrator permission.", color=0xE02B2B)
            await context.send(embed=embed)
        else:
            try:
                embed = discord.Embed(description=f"**{member}** was kicked by **{context.author}**!",color=0xBEBEFE,)
                embed.add_field(name="Reason:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(f"You were kicked from **{context.author}** from **{context.guild.name}** !\nReason: {reason}")

                except:
                    pass
                await member.kick(reason=reason)
            except:
                embed = discord.Embed(description="An error occurred while trying to kick the user. Make sure my role is above the role of the user you want to kick.", color=0xE02B2B)
                await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))

