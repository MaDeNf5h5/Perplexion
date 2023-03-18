import os
import ssl
import json
import time
import motor.motor_asyncio

from multiprocessing import Process, freeze_support

import disnake
from disnake.ext import commands

from motor.motor_asyncio import AsyncIOMotorClient

bot = commands.Bot(command_prefix="ladno", test_guilds=[952334521091637278], intents=disnake.Intents.all())
bot.icon = ":coin:"

mongo = AsyncIOMotorClient(
    "mongodb+srv://cruiseqq:kjlKmLpLEktM1iLN@cluster0.7bxmwfm.mongodb.net/?retryWrites=true&w=majority",
    serverSelectionTimeoutMS=10000
)

bot.economy = mongo.bot.economy
bot.inventar = mongo.bot.inventar
bot.roles = mongo.bot.roles
bot.voice = mongo.bot.voice
bot.messages = mongo.bot.messages
bot.voice_active = mongo.bot.voice_active
bot.marry = mongo.bot.marry
bot.marry_voice = mongo.bot.marry_voice 
bot.name_love_room = mongo.bot.name_love_room

@bot.event
async def on_ready() -> None:
    guild = bot.get_guild(606206371951542284)
    role = guild.get_role(1007943635242860655)
    for i in guild.members:
        await i.add_roles(role)

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run("")
