from discord.ext import commands
from discord.ext.commands.context import Context


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def restartbot(self, ctx: Context) -> None:
        await ctx.channel.send('Rebooting!')
        await self.bot.logout()
