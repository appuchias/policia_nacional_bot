from typing import Union
import discord
from discord.ext import commands


class Carguai(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    async def di(self, ctx, channel: Union[discord.TextChannel, int], *message: str) -> None:
        if type(channel) == int:
            channel = self.client.fetch_channel(channel)
        await channel.send(message)


def setup(client):
    client.add_cog(Carguai(client))
