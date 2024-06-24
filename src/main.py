import os

import discord
from dotenv import load_dotenv

from src.discord_bot import MyClient

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = MyClient(intents=intents)

if __name__ == "__main__":
    client.run(TOKEN)
