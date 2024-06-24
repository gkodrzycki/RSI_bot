import logging
import os

import discord
from discord.ext import tasks
from dotenv import load_dotenv

from src.trading_utils import calculate_rsi, fetch_kline_data

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

load_dotenv()
GUILD_NAME = os.getenv("DISCORD_GUILD_NAME")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        for guild in self.guilds:
            if guild.name == GUILD_NAME:
                break

        logger.info(
            f"{self.user} is connected to the following guild (discord server): {guild.name}(id: {guild.id})"
        )

        self.channel = self.get_channel(CHANNEL_ID)
        logger.info(f"Assigned channel: {self.channel}")

        self.check_rsi.start()

    # We need to take care of Discord API limit as well
    @tasks.loop(seconds=1)
    async def check_rsi(self):
        await self.wait_until_ready()
        data = await fetch_kline_data()
        rsi = calculate_rsi(data)
        last_rsi = rsi.iloc[-1]

        if last_rsi > 70:
            await self.channel.send(f"RSI is over 70: {last_rsi}")
        elif last_rsi < 30:
            await self.channel.send(f"RSI is below 30: {last_rsi}")

    @check_rsi.before_loop
    async def before_check_rsi(self):
        await self.wait_until_ready()
