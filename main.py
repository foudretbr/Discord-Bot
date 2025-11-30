import logging
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

class LoggingFormatter(logging.Formatter):
    # Colors in ANSI code, refer to https://talyian.github.io/ansicolors/
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)


logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())
# File handler
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=PREFIX, intents=intents)
        self.logger = logger

    async def load_cogs(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                extension = file[:-3]
                try:
                    await self.load_extension(f'cogs.{extension}')
                    self.logger.info(f'Loaded extension: {extension}')
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    self.logger.error(
                        f'Failed to load extension {extension}\n{exception}'
                    )

    async def setup_hook(self):
        self.logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        await self.load_cogs()

    async def on_ready(self):
        self.logger.info(f'{self.user} (ID: {self.user.id} ) is ready.')

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

bot = MyBot()
bot.run(TOKEN)