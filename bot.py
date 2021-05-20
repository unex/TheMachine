import os
from typing import Optional

import discord
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")

description = '''The Machine'''
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$$', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

    await bot.change_presence(
        status = discord.Status.dnd,
        activity = discord.Activity(
            type = discord.ActivityType.watching,
            name = "you"
        )
    )

@bot.check
def check_commands(ctx):
    return bot.is_owner(ctx.author) or ctx.guild and ctx.author.guild_permissions.administrator

@bot.command()
async def say(ctx, channel: Optional[discord.TextChannel], *, text: str):
    if not channel:
        channel = ctx.channel

    await channel.send(text)


bot.run(TOKEN)
