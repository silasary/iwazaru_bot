import sys
from typing import Dict

import discord
from discord.errors import Forbidden
from discord.guild import Guild
from discord.message import Message
from discord.reaction import Reaction
from discord.user import User

from shared import configuration
from shared.limited_dict import LimitedSizeDict

from . import warnings
from .messagedata import MessageData


class Bot(discord.Client):
    def __init__(self) -> None:
        super().__init__()
        self.cache: Dict[Message, MessageData] = LimitedSizeDict(size_limit=1000)

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
                await message.add_reaction("🙊")
                self.cache[message] = data
            except Forbidden:
                pass
        if message.content == '!restartbot':
            await message.channel.send('Rebooting!')
            await self.logout()
            sys.exit()

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
            await after.remove_reaction("🙊", self.user)
            if data.response_message is not None:
                await data.response_message.delete()

    async def on_reaction_add(self, reaction: Reaction, author: User) -> None:
        c = reaction.count
        if reaction.me:
            c = c - 1
        if reaction.message.author == self.user:
            if c > 0 and not reaction.custom_emoji and reaction.emoji == "❎":
                await reaction.message.delete()
        elif c > 0 and reaction.emoji == "🙊":
            data = self.cache.get(reaction.message, None)
            if data is None:
                return
            if data.response_message is None and data.response_text is not None:
                data.response_message = await reaction.message.channel.send(data.response_text)
                await data.response_message.add_reaction("❎")

    async def on_server_join(self, server: Guild) -> None:
        await server.default_channel.send(":see_no_evil: :hear_no_evil: :speak_no_evil:")
        await server.default_channel.send("If I react to a message, click on that reaction to see more details.")

    async def on_ready(self) -> None:
        print('Logged in as {username} ({id})'.format(username=self.user.name, id=self.user.id))
        print('Connected to {0}'.format(', '.join([server.name for server in self.guilds])))
        print('--------')

def init() -> None:
    client = Bot()
    client.init()

if __name__ == "__main__":
    init()
