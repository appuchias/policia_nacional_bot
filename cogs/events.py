import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    # @commands.Cog.listener(name="on_message")
    # async def on_msg(self, message):
    #     if message.embeds or message.author == self.client.user or message.author.bot:
    #         return

    @commands.Cog.listener()
    async def on_member_join(self, member):
        new = discord.utils.get(member.guild.roles, name="Truquero")
        await member.add_roles(new)
        await member.send(f"Bienvenido al server **{member.guild}**!")
        channel = discord.utils.get(member.guild.channels, name="🎊-bienvenida")
        await channel.send(f"{member.mention} se acaba de unir! :tada:")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        user = member
        channel = discord.utils.get(member.guild.channels, name="huidas")
        await channel.send(f"{user} se acaba de ir, parece que no lo pasaba bien D:")


def setup(client):
    client.add_cog(Events(client))
