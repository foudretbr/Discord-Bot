import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

class Moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command(name="kick", description="Kick an user out of the server.")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @app_commands.describe(user="The user to kick", reason="The reason why the user should be kicked")
    async def kick(self, context: Context, user: discord.User, *, reason: str = "Not specified"):
        """
        Kick an user from the server.

        :param context: The hybrid command context.
        :param user: The user to kick.
        :param reason: The reason why the user should be kicked. 
        """
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

    @commands.hybrid_command(name="ban", description="A command for ban a user from the server.")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @app_commands.describe(user="The user to ban", reason= "The reason why the user should be banned")
    async def ban(self, context: Context, user : discord.User, *, reason: str = "The reason why the user should be ban."):
        """
        Ban an user from the server.
        
        :param context: The hybrid command context.
        :param user: The user who should be banned.
        :param reason: The reason why the user should be banned.
        """
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(user.id)
        if member.guild_permissions.administrator:
            embed = discord.Embed(description="User has administrator permission.", color=0xE02B2B)
            await context.send(embed=embed)
        else:
            try:
                embed = discord.Embed(description=f"**{member}** was banned by **{context.author}**!",color=0xBEBEFE,)
                embed.add_field(name="Reason:", value=reason)
                await context.send(embed=embed)
                try:
                    await member.send(f"You were banned from **{context.guild.name}** by **{context.author}** !\nReason: {reason}")
                except:
                    pass
                await member.ban(reason=reason)
            except:
                embed = discord.Embed(description="An error occurred while trying to ban the user. Make sure my role is above the role of the user you want to ban.", color=0xE02B2B)
                await context.send(embed=embed)

    @commands.hybrid_command(name="clear", description="Clear a specified number of messages in the channel.")
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @app_commands.describe(amount="The number of messages to clear")
    async def clear(self, context: Context, amount: int):
        """
        Clear a specified number of messages in the channel.
        
        :param context: The hybrid command context.
        :param amount: The number of messages that should be deleted.
        """
        await context.send(f"Deleting {amount} messages...")
        await context.channel.purge(limit=amount+2) # +2 to include the command message and the "Deleting amount message..." message
        embed = discord.Embed(description=f"✅ | Cleared {amount} messages !", color=0xBEBEFE)
        await context.channel.send(embed=embed, delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))