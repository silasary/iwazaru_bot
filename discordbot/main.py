import logging
from typing import Dict

from naff.client import Client
from naff.api.events import MessageCreate, MessageReactionAdd, MessageUpdate
from naff.client.errors import Forbidden
from naff.models import Intents, listen, Snowflake_Type

from shared import configuration
from shared.limited_dict import LimitedSizeDict

from . import warnings
from .messagedata import MessageData


msg_cache: Dict[Snowflake_Type, MessageData] = LimitedSizeDict(
    size_limit=1000,
)

logging.basicConfig()
cls_log = logging.getLogger('naff')
cls_log.setLevel(logging.WARNING)


class Bot(Client):
    sentry_token = 'https://83766626d7a64c1084fd140390175ea5@sentry.io/1757452'

    def __init__(self) -> None:
        super().__init__(intents=Intents(Intents.DEFAULT | Intents.MESSAGES | Intents.GUILD_MESSAGE_CONTENT))
        super().load_extension('dis_taipan.sentry')
        try:
            super().load_extension('dis_taipan.updater')
        except ImportError:
            logging.warning('Could not load updater extension.')

    @listen()
    async def on_message_create(self, event: MessageCreate) -> None:
        if event.message.author == self.user:
            return
        if event.message.author.bot:
            return
        data = MessageData()
        data.response_text = warnings.parse_message(event.message.content)
        if data.response_text is not None:
            try:
                await event.message.add_reaction('🙊')
                msg_cache[event.message.id] = data
            except Forbidden:
                pass

    @listen()
    async def on_message_update(self, event: MessageUpdate) -> None:
        if event.after.author == self.user:
            return
        if event.after.author.bot:
            return

        data = msg_cache.get(event.after.id, None)
        if data is None:
            return

        data.response_text = warnings.parse_message(event.after.content)
        prev_reacted = [r for r in event.after.reactions if r.me]
        if data.response_text is None and prev_reacted:
            await event.after.remove_reaction('🙊', self.user)
            if data.response_message is not None:
                await data.response_message.delete()

    @listen()
    async def on_message_reaction_add(self, event: MessageReactionAdd) -> None:
        for i in range(len(event.message.reactions)):
            r = event.message.reactions[i]
            if r.emoji == event.emoji:
                reaction = r
                break
        else:
            return
        c = reaction.count
        if reaction.me:
            c = c - 1

        if reaction.message.author.id == self.user.id:
            if c > 0 and reaction.emoji.name == '❎':
                await reaction.message.delete()
        elif c > 0 and reaction.emoji.name == '🙊':
            data = msg_cache.get(reaction.message.id, None)
            if data is None:
                response_text = warnings.parse_message(event.message.content)
                if response_text is None:
                    return
                data = MessageData()
                data.response_text = response_text
                msg_cache[reaction.message.id] = data

            if data.response_message is None and data.response_text is not None:
                data.response_message = await reaction.message.channel.send(
                    data.response_text,
                )
                await data.response_message.add_reaction('❎')

    # @listen()  # dis-snake doesn't have an analogue for this yet.
    # async def on_server_join(event) -> None:
    #     for channel in server.text_channels:
    #         try:
    #             await channel.send(':see_no_evil: :hear_no_evil: :speak_no_evil:')
    #             await channel.send('If I react to a message, click on that reaction to see more details.')
    #             await channel.send('I have no moderation functionality, and only exist to help with self-improvement.')
    #             return
    #         except Forbidden:
    #             pass

    @listen()
    async def on_ready(self) -> None:
        print(
            'Logged in as {username} ({id})'.format(
                username=self.user,
                id=self.user.id,
            ),
        )
        print(
            'Connected to {}'.format(
                ', '.join([server.name for server in self.guilds if server]),
            ),
        )
        print('--------')


client = Bot()


def init() -> None:
    client.start(configuration.get('token'))


if __name__ == '__main__':
    init()
