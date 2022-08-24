from typing import Optional
from naff.models import Message

from munch import Munch

__all__ = 'MessageData'


class MessageData(Munch):
    def __init__(self) -> None:
        self.response_message: Optional[Message] = None
        self.response_text: Optional[str] = None
