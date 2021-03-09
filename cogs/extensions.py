import discord
from discord.ext import commands


class Extensions(commands.Cog):
    def __init__(self, client):
        self.client = client

    ext_prefix = "cogs."

    # Commands
    # Load an extension
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension: str):
        self.client.load_extension(self.ext_prefix + extension)
        await ctx.send(f"Cargada!")

    # Unload an extension
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension: str):
        self.client.unload_extension(self.ext_prefix + extension)
        await ctx.send(f"Descargada!")

    # Reload an extension
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension: str):
        print("reload " + extension)
        self.client.unload_extension(self.ext_prefix + extension)
        await ctx.send(f"Descargada!")
        self.client.load_extension(self.ext_prefix + extension)
        await ctx.send(f"Recargada!")


def setup(client):
    client.add_cog(Extensions(client))
