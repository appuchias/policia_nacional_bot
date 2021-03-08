import asyncio, json, discord
from discord.ext import commands


class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    # When a message is sent
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.channel.id == 818568854161588324:
            return
        bad_words = [
            "puta",
            "puto",
            "gilipollas",
            "hijo de",
            "cabron",
            "cabrón",
            "pvta",
            "pvto",
            "pta",
            "pto",
            "p*to",
            "p*ta",
            "asshole",
        ]
        user = message.author
        for word in bad_words:
            if word in message.content.lower():
                try:
                    await user.send(f"Ey! no digas esas cosas! (||{word}||)")
                except discord.errors.Forbidden:
                    await message.channel.send(f"Eso no se dice eh {message.author.mention}")
                finally:
                    await message.delete()
                # await self.warning(user, user, f"Used a bad word ({word})")

    # Commands
    # Bulk message delete
    @commands.command()
    @commands.has_role("MOD")
    async def clear(self, ctx, number: int = 5):
        n = number
        if int(n) > 100:
            await ctx.send("Demasiados mensajes para eliminar...")
            return
        await ctx.channel.purge(limit=(int(n) + 1))
        msg = await ctx.send(f"{str(n)} mensaje(s) eliminados!")
        print(f"{str(n)} messages cleared in #{ctx.channel.name}")
        await msg.delete(delay=2)

    # Kick someone
    @commands.command()
    @commands.has_role("MOD")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} kickeado!")

        await ctx.message.delete(delay=2)

    # Ban someone
    @commands.command()
    @commands.has_role("MOD")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} baneado!")

        await ctx.message.delete(delay=2)

    # #Unban someone
    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def unban(self, ctx, *, member):
    #     banned_users = await ctx.guild.bans()
    #     name, discr = member.split('#')
    #     for ban_entry in banned_users:
    #         user = ban_entry.user
    #         if(user.name, user.discriminator) == (name, discr):
    #             await ctx.guild.unban(user)
    #
    #     await ctx.send(f'{member} desbaneado!')
    #     await ctx.message.delete(delay=2)

    @commands.command()
    @commands.has_role("MOD")
    async def mute(self, ctx, user: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muteado")
        await user.add_roles(muted_role)

    # @commands.command()
    # @commands.has_role("MOD")
    # async def tmute(self, ctx, user: discord.Member, n:int):
    #     muted_role = discord.utils.get(ctx.guild.roles, name="Muted role")
    #     await user.add_roles(muted_role)
    #
    #     await asyncio.sleep(n*60)
    #     await user.remove_roles(muted_role)

    # To report members for more irrelevant things than a warn
    @commands.command()
    @commands.has_role("MOD")
    async def report(self, ctx, who: discord.Member, *, reason="no reason"):
        author = ctx.author
        channel = discord.utils.get(ctx.guild.channels, name="reports")
        appu = discord.utils.get(ctx.guild.members, id=455321214525767680)

        with open("logs/reports.json") as r:
            reports = json.loads(r.read())

        if not str(who.id) in reports:
            reports[str(who.id)] = 0
        reports[str(who.id)] += 1

        case = 0
        for n in reports:
            case += reports[n]
        await appu.send(
            f"{author.mention} reported {who.mention} for **[{reason}]** and now has **[{reports[str(who.id)]}]** reports!"
        )
        await channel.send(
            f"▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\nCase **{case}**:\n - Member: **{who}**\n - Actual reports: **{reports.get(str(who.id))}**\n - Reason: *{reason}*"
        )

        if reports.get(str(who.id)) >= 3:
            await appu.send(f"[{who}] has [{reports.get(str(who.id))}] reports! Be aware!")

        with open("logs/reports.json", "w") as w:
            w.write(json.dumps(reports, indent=4))

        await ctx.message.delete(delay=2)

    # Warn group
    @commands.group(hidden=True)
    async def warn(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Este comando necesita parámetros extra!")

    @warn.command()
    @commands.has_permissions()
    async def user(self, ctx, user: discord.Member, *, reason: str = None):
        await self.warning(ctx, user, reason)

        await ctx.send(f"{user.name} fue alertado por {ctx.author}")
        await ctx.message.delete(delay=2)

    @warn.command()
    async def claim(self, ctx, *, reason: str):
        channel = discord.utils.get(ctx.guild.channels, name="disputas")
        with open("logs/warns.json", "r") as f:
            warns = json.load(f)
        if channel != None:
            await channel.send(
                f"{ctx.author.mention} ha disputado su último warn, de un total de [{warns[str(ctx.author.id)]}] con el motivo de [{reason}]"
            )
            await ctx.message.delete(delay=2)

    # # Log
    # async def log(self, ctx, msg):
    #     channel = discord.utils.get(ctx.guild.text_channels, name="log")
    #     if channel in ctx.guild.text_channels:
    #         pass
    #     else:
    #         await ctx.send("Error 404. Channel not found")
    #         return

    #     await channel.send(msg)
    #     print(f"Log: {msg}")

    #     with open("modlog.txt", "a") as f:
    #         f.write(f"Log: {msg}\n")


def setup(client):
    client.add_cog(Mod(client))
