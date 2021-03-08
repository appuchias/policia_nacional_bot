import discord
from discord.ext import commands
import random
from checks import channel


# Comandos de uso en el chat
class Chat(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.command()
    @commands.check(channel)
    async def suma(self, ctx, args: commands.Greedy[int]):
        "Suma varios números"
        await ctx.send(sum(args))

    @commands.command()
    @commands.check(channel)
    async def multiplica(self, ctx, args: commands.Greedy[int]):
        "Multiplica varios números"
        output = 1
        for n in args:
            output *= n
        await ctx.send(output)

    @commands.command()
    @commands.check(channel)
    async def invierte(self, ctx, *, args):
        "Invierte el orden de las palabras del texto que mandes"
        output = " "
        for word in args.split(" "):
            output += word
            output += " "
        output = output[::-1]
        await ctx.send(output)

    @commands.command()
    @commands.check(channel)
    async def moneda(self, ctx, repetitions: int = 1):
        "Lanza n monedas y obtén el resultado"
        if repetitions > 0 and repetitions <= 20:
            embed = discord.Embed(
                title="Moneda",
                description=f"{repetitions} repeticiones",
                color=0xF1C40F,
            )
            for cnt in range(repetitions):
                n = random.choice([True, False])
                if n:
                    v = "CARA! :adult:"

                else:
                    v = "CRUZ! :x:"

                if random.randint(0, 1000) == 1:
                    v = "CANTOOOOO!!! :tada::tada:"

                embed.add_field(name=f"{cnt+1}/{repetitions}", value=v)

            if repetitions > 5:
                embed.set_thumbnail(
                    url="https://i.pinimg.com/originals/d7/49/06/d74906d39a1964e7d07555e7601b06ad.gif"
                )
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f"Por favor, no te pases, {repetitions} está por encima de 20, mi máximo de repeticiones del comando! :warning:"
            )


def setup(client):
    client.add_cog(Chat(client))
