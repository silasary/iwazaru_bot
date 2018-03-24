from discord import Message
from munch import Munch

__all__ = ('MessageData')

class MessageData(Munch):
    def __init__(self):
        self.response_message: Message = None
        self.response_text: str = None
