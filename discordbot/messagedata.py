from typing import Optional

from munch import Munch

from discord import Message

__all__ = ('MessageData')

class MessageData(Munch):
    def __init__(self) -> None:
        self.response_message: Message = None
        self.response_text: Optional[str] = None
