import requests
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ext.commands import Context

class PexelsAPI(commands.Cog, name="troll"):
    """Class to use PexelsAPI"""
    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(PexelsAPI(bot))