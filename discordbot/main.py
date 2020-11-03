from typing import Dict

from discord.ext import commands
from discord.errors import Forbidden
from discord.guild import Guild
from discord.message import Message
from discord.reaction import Reaction
from discord.user import User

from . import warnings, cmd_cog
from .messagedata import MessageData
from shared import configuration
from shared.limited_dict import LimitedSizeDict


class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=commands.when_mentioned_or('🙊'))
        self.cache: Dict[Message, MessageData] = LimitedSizeDict(
            size_limit=1000,
        )
        self.help_command.get_ending_note = self.help_footer

    def init(self) -> None:
        self.run(configuration.get('token'))

    async def on_message(self, message: Message) -> None:
        if message.author == self.user:
            return
        if message.author.bot:
            return
        data = MessageData()
        data.response_text = warnings.parse_message(message.content)
        if data.response_text is not None:
            try:
                await message.add_reaction('🙊')
                self.cache[message] = data
            except Forbidden:
                pass
        await self.process_commands(message)

    async def on_message_edit(self, before: Message, after: Message) -> None:
        if after.author == self.user:
            return
        if after.author.bot:
            return

        data = self.cache.get(after, None)
        if data is None:
            return

        data.response_text = warnings.parse_message(after.content)
        prev_reacted = [r for r in after.reactions if r.me]
        if data.response_text is None and prev_reacted:
            await after.remove_reaction('🙊', self.user)
            if data.response_message is not None:
                await data.response_message.delete()

    async def on_reaction_add(self, reaction: Reaction, author: User) -> None:
        c = reaction.count
        if reaction.me:
            c = c - 1
        if reaction.message.author == self.user:
            if c > 0 and not reaction.custom_emoji and reaction.emoji == '❎':
                await reaction.message.delete()
        elif c > 0 and reaction.emoji == '🙊':
            data = self.cache.get(reaction.message, None)
            if data is None:
                return
            if data.response_message is None and data.response_text is not None:
                data.response_message = await reaction.message.channel.send(
                    data.response_text,
                )
                await data.response_message.add_reaction('❎')

    async def on_server_join(self, server: Guild) -> None:
        for channel in server.text_channels:
            try:
                await channel.send(':see_no_evil: :hear_no_evil: :speak_no_evil:')
                await channel.send('If I react to a message, click on that reaction to see more details.')
                await channel.send('I have no moderation functionality, and only exist to help with self-improvement.')
                return
            except Forbidden:
                pass

    async def on_ready(self) -> None:
        print(
            'Logged in as {username} ({id})'.format(
                username=self.user.name,
                id=self.user.id,
            ),
        )
        print(
            'Connected to {}'.format(
                ', '.join([server.name for server in self.guilds]),
            ),
        )
        print('--------')

    def help_footer(self) -> str:
        return "I really don't have any commands.  If you want an example of what I can do, just say 'Stupid bot', and click on the 🙊.\n\n"


def init() -> None:
    client = Bot()
    client.load_extension("jishaku")
    client.add_cog(cmd_cog.Commands(client))
    client.init()


if __name__ == '__main__':
    init()
