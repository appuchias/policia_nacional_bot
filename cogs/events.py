import discord
from discord.ext import commands
from discord.role import Role


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        guild = await self.client.fetch_guild(815689898756407307)  # SrtoCarguai
        channel = await self.client.fetch_channel(815689900719734835)  # #🎊-bienvenida
        truquero = guild.get_role(815748222210277406)  # Truquero
        assert type(truquero) == discord.Role

        await member.add_roles(truquero)
        try:
            await member.send(f"Bienvenido al server **{member.guild}**!")
        finally:
            await channel.send(f"{member.mention} se acaba de unir! :tada:")

    # @commands.Cog.listener()
    # async def on_member_remove(self, member: discord.Member):
    #     channel = await self.client.fetch_channel(818569618770886697)  # #huidas
    #     await channel.send(f"{member.mention} se acaba de ir D:")


def setup(client):
    client.add_cog(Events(client))
