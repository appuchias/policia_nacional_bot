from typing import Union
import discord
from discord.channel import TextChannel
from discord.ext import commands
import asyncio

from discord.ext.commands.core import command


class Carguai(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def di(
        self,
        ctx,
        message_channel: Union[discord.TextChannel, int] = 571380940664995842,
        *message: str,
    ) -> None:
        channel = (
            message_channel
            if type(message_channel) == discord.TextChannel
            else self.client.fetch_channel(message_channel)
        )
        message = '"*' + " ".join(message) + '*"'
        await ctx.send(message)
        msg = await ctx.send("Correcto? (Si no es correcto espera un minuto)")
        await msg.add_reaction("👍")

        def check(reaction, user):
            return (
                reaction.message.id == msg.id
                and user.id == ctx.message.author.id
                and str(reaction.emoji) == "👍"
            )

        try:
            reaction, user = await self.client.wait_for("reaction_add", timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Tiempo agotado")
            await msg.clear_reactions()
        else:
            await channel.send(message)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def die(
        self, ctx, message_channel: Union[discord.TextChannel, int], *message: str,
    ) -> None:
        channel = (
            message_channel
            if type(message_channel) == discord.TextChannel
            else self.client.fetch_channel(message_channel)
        )

        msg = [word.replace("\n", "llllll") for word in message]

        embed = discord.Embed(
            description=f'```{" ".join(msg)}```',
            color=discord.Color.blurple(),
        )
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(Carguai(client))
