import sys
from typing import Dict

import discord
from discord.errors import Forbidden
from discord.message import Message
from discord.reaction import Reaction
from discord.server import Server
from discord.user import User

from shared import configuration
from shared.limited_dict import LimitedSizeDict

from . import warnings
from .messagedata import MessageData


class Bot:
    def __init__(self) -> None:
        self.client = discord.Client()
        self.cache: Dict[Message, MessageData] = LimitedSizeDict(size_limit=1000)

    def init(self) -> None:
        self.client.run(configuration.get('token'))

BOT = Bot()

@BOT.client.event
async def on_message(message: Message) -> None:
    if message.author == BOT.client.user:
        return
    if message.author.bot:
        return
    data = MessageData()
    data.response_text = warnings.parse_message(message.content)
    if data.response_text is not None:
        try:
            await BOT.client.add_reaction(message, "🙊")
            BOT.cache[message] = data
        except Forbidden:
            pass
    if message.content == '!restartbot':
        await BOT.client.send_message(message.channel, 'Rebooting!')
        await BOT.client.logout()
        sys.exit()

@BOT.client.event
async def on_message_edit(before: Message, after: Message) -> None:
    if after.author == BOT.client.user:
        return
    if after.author.bot:
        return

    data = BOT.cache.get(after, None)
    if data is None:
        return

    data.response_text = warnings.parse_message(after.content)
    prev_reacted = [r for r in after.reactions if r.me]
    if data.response_text is None and prev_reacted:
        await BOT.client.remove_reaction(after, "🙊", BOT.client.user)
        if data.response_message is not None:
            await BOT.client.delete_message(data.response_message)

@BOT.client.event
async def on_reaction_add(reaction: Reaction, author: User) -> None:
    c = reaction.count
    if reaction.me:
        c = c - 1
    if reaction.message.author == BOT.client.user:
        if c > 0 and not reaction.custom_emoji and reaction.emoji == "❎":
            await BOT.client.delete_message(reaction.message)
    elif c > 0 and reaction.emoji == "🙊":
        data = BOT.cache.get(reaction.message, None)
        if data is None:
            return
        if data.response_message is None and data.response_text is not None:
            await BOT.client.send_typing(reaction.message.channel)
            data.response_message = await BOT.client.send_message(reaction.message.channel, data.response_text)
            await BOT.client.add_reaction(data.response_message, "❎")

@BOT.client.event
async def on_server_join(server: Server) -> None:
    await BOT.client.send_message(server.default_channel, ":see_no_evil: :hear_no_evil: :speak_no_evil:")
    await BOT.client.send_message(server.default_channel, "If I react to a message, click on that reaction to see more details.")

@BOT.client.event
async def on_ready() -> None:
    print('Logged in as {username} ({id})'.format(username=BOT.client.user.name, id=BOT.client.user.id))
    print('Connected to {0}'.format(', '.join([server.name for server in BOT.client.servers])))
    print('--------')

def init() -> None:
    BOT.init()

if __name__ == "__main__":
    init()
