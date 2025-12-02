import requests, random, os, discord
from pexels_api import API
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

load_dotenv()

API_KEY = os.getenv("PEXELS_API_KEY")
api = API(API_KEY)

class PexelsAPI(commands.Cog, name="troll"):
    """Class to use PexelsAPI"""
    def __init__(self, bot):
        self.bot = bot
        self.key = API_KEY

    @commands.hybrid_command(name="img", description="Return a random image of a keyword.")
    @commands.bot_has_permissions(send_messages=True)
    @app_commands.describe(keyword="A keyword to find a type of images in Pexels.", amount="The amount of image to generate.")
    async def img(self, context : Context, keyword : str, *,  amount : int):
        """
        A command who return images of pexels, with keyword and the amount of images.
        
        :param context: The hybrid command context.
        :Type context: Context
        :param keyword: The keyword to search images.
        :type keyword: str
        :param amount: The amount of images to search, maximum = 100.
        :type amount: int
        """
        if amount > 4:
            await context.send(f"The maximal amount of images per request is 4 !")
            return

        for i in range(amount):
            api.search(keyword, page=1, results_per_page=100)
            photos = api.get_entries()
            if not photos:
                await context.send(f"No images found for {keyword}")
                return
            else:
                photo = random.choice(photos)
                image_url = photo.original
                await context.send(image_url)
    
    @commands.hybrid_command(name="nga", description="A command who return a random image of a black.")
    @commands.bot_has_permissions(send_messages=True)
    @app_commands.describe(amount = "The amount of image of black to research.")
    async def nga(self, context: Context, amount : int):
        """
        Command to search image with a racist keyword, to humour, for an amount.
        
        :param context: The hybrid command context.
        :type context: Context
        :param amount: The amount of images to search in Pexels.
        :type amount: int
        """
        if amount > 4:
            await context.send('Amount max is 4')
            return
        
        for i in range(amount):
            api.search("nigger", page=1, results_per_page=100)
            photos = api.get_entries()
            if not photos:
                await context.send(f"No images found")
                return
            else:
                photo = random.choice(photos)
                image_url = photo.original
                await context.send(image_url)        



async def setup(bot):
    await bot.add_cog(PexelsAPI(bot))