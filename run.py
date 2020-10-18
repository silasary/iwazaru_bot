import sentry_sdk

from discordbot import main

sentry_sdk.init('https://83766626d7a64c1084fd140390175ea5@sentry.io/1757452')
main.init()
