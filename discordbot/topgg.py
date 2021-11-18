import dbl
from discord.ext import commands

from shared import configuration


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = configuration.get('dbl_token')
        if not self.token:
            return
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)

    # pylint: disable=no-self-use
    async def on_guild_post(self):
        print('Server count posted successfully')


def setup(bot):
    bot.add_cog(TopGG(bot))
