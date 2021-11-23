from typing import Optional
from dis_snek.models.discord_objects.message import Message

from munch import Munch

__all__ = 'MessageData'


class MessageData(Munch):
    def __init__(self) -> None:
        self.response_message: Message = None
        self.response_text: Optional[str] = None
