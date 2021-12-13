import logging
import sentry_sdk

from discordbot import main


def sentry_filter(event: dict[str, Any], hint: dict[str, Any]):  # type: ignore
    if 'log_record' in hint:
        record: logging.LogRecord = hint['log_record']
        if 'dis.snek' in record.name and '/commands/permissions: 403' in record.message:
            return None

    if 'exc_info' in hint:
        exc_type, exc_value, tb = hint['exc_info']
        if isinstance(exc_value, OSError):
            return None
    return event


sentry_sdk.init('https://83766626d7a64c1084fd140390175ea5@sentry.io/1757452', before_send=sentry_filter)
main.init()
