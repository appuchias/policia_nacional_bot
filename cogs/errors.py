import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Te falta un elemento necesario en el comando! :anger:")

        elif isinstance(error, commands.MissingRole):
            await ctx.send(f"Necesitas otro rol!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send(f"Necesitas tener rol!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"No tienes el permiso necesario!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.UnexpectedQuoteError):
            await ctx.send(f"Te sobran comillas!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Parámetro inválido!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f"Esto no funciona en DM!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.CheckFailure):
            msg = await ctx.send(f"No has mandado el mensaje en el canal de bot! :confused:")
            await ctx.message.delete(delay=2)
            await msg.delete(delay=2)

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(
                f"El comando no existe o lo has escrito mal :confused:\n*(Error: {error})*"
            )

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f"Comando desactivado por Mr.Appu")

        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"Problema interno del comando :confused:\n*(Error: {error})*")
            print("Error interno: " + str(error))

        elif isinstance(error, commands.TooManyArguments):
            await ctx.send(f"El error lo dice todo.:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.NotOwner):
            await ctx.send(
                f"Para eso hace falta ser el propietario del bot!:confused:\n*(Error: {error})*"
            )

        elif isinstance(error, commands.ExtensionError):
            await ctx.send(f"Error en una extensión!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send(f"Extensión ya cragada!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send(f"Extensión no cargada:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.NoEntryPointError):
            await ctx.send(f"Falta el setup de la extensión!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.ExtensionFailed):
            await ctx.send(f"Error en el setup de la extensión!:confused:\n*(Error: {error})*")

        elif isinstance(error, commands.ExtensionNotFound):
            await ctx.send(f"Esa extensión ni siquiera existe:confused:\n*(Error: {error})*")

        # elif isinstance(error, ):
        #     await ctx.send(f":confused:\n*(Error: {error})*")
        #


def setup(client):
    client.add_cog(Errors(client))
