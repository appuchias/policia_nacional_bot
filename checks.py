import discord
from discord.ext import commands

bot_channel_id = 818568854161588324


async def channel(ctx):
    return ctx.channel.id == bot_channel_id
