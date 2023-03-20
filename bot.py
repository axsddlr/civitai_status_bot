import asyncio
import json

import discord

from util.uptime_list import process_uptime_list

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config["DISCORD_TOKEN"]
CHANNEL_ID = config["DISCORD_CHANNEL_ID"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def check_website_status():
    while True:
        channel = client.get_channel(CHANNEL_ID)
        percentage_dict = await process_uptime_list()
        issues_found = False
        for key, value in percentage_dict.items():
            if float(value.rstrip("%")) < 85:
                issues_found = True
                await channel.send(f"Issues detected with {key}: {value}")
        if not issues_found:
            await channel.send("Services are good")
        await asyncio.sleep(60)


@client.event
async def on_ready():
    print("Bot is ready")
    await check_website_status()


client.run(TOKEN)
