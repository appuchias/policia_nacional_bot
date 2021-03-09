import discord, pytz, os
from discord.ext import commands
from datetime import datetime as dt
from rich.traceback import install
from os import getenv
from dotenv import load_dotenv
from checks import channel

load_dotenv()
install()


# VARS
prefix = "!"
client = commands.Bot(
    command_prefix=prefix,
    help_command=commands.MinimalHelpCommand(
        sort_commands=False,
        aliases_heading="También: ",
        no_category="General",
        dm_help=None,
        dm_help_treshold=500,
    ),
)
tz = pytz.timezone("Europe/Madrid")

# On ready
@client.event
async def on_ready():
    print("Connected as:")
    print("{}: {}".format(client.user.name, client.user.id))
    print(f"Prefix: {prefix}")
    print(dt.now(tz).strftime("%H:%M:%S %d/%m/%Y"))
    print("--------------")
    game = discord.Activity(
        name=f"{prefix}help | {client.user.name} | By Appu",
        type=discord.ActivityType.watching,
    )
    await client.change_presence(activity=game, status=discord.Status.online)


@client.command(aliases=["test"])
@commands.check(channel)
async def ping(ctx):
    "Comando de prueba"
    await ctx.send(f"Pong! ||( Ping de {round(client.latency*1000)}ms )||")


# Emergency logout
@client.command(hidden=True)
@commands.check(commands.is_owner())
async def logout(ctx):
    msg = await ctx.send("Desconectando...")
    await ctx.delete(delay=1)
    await msg.delete(delay=2)
    await client.close()


# Load all extensions
extensions = []
for filename in os.listdir("./cogs"):
    if str(filename).endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        extensions.append(filename[:-3])
print(f"{extensions} loaded!")

# Bot run
if __name__ == "__main__":
    client.run(getenv("TOKEN"))