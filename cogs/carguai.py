from typing import Union
import discord
from discord.ext import commands
import asyncio


class Carguai(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def di(
        self, ctx, channel: Union[discord.TextChannel, int] = 571380940664995842, *message: str
    ) -> None:
        if type(channel) == int:
            channel = self.client.fetch_channel(channel)
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


def setup(client):
    client.add_cog(Carguai(client))
