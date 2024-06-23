import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Habilita permisos para leer mensajes

bot = commands.Bot(command_prefix='!', intents=intents)

# Cargar extensiones al iniciar el bot
initial_extensions = ['cogs.example']

async def load_extensions():
    for extension in initial_extensions:
        await bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

async def main():
    await load_extensions()
    await bot.start(TOKEN)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
