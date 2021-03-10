import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        new = await self.client.fetch_role(815748222210277406)  # Truquero
        channel = await self.client.fetch_channel(815689900719734835)  # #🎊-bienvenida
        await member.add_roles(new)
        try:
            await member.send(f"Bienvenido al server **{member.guild}**!")
        finally:
            await channel.send(f"{member.mention} se acaba de unir! :tada:")

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = await self.client.fetch_channel(818569618770886697)  # #huidas
        await channel.send(f"{member.name}#{member.discriminator} se acaba de ir D:")


def setup(client):
    client.add_cog(Events(client))
