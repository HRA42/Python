import hikari  # Import the hikari module (Discord API)
import lightbulb  # Import the lightbulb module (Eventhandler)
from decouple import config  # read env variables for token
import sentry_sdk  # get errors on runtime via mail
import aiohttp  # handle datastore and api requests

# Init Sentry to catch errors on runtime
sentry_sdk.init(
    "https://9b6ee33a6070436f90226f3f97f5809b@o1034905.ingest.sentry.io/6001551",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

# Init Bot with token and guild IDs
bot = lightbulb.BotApp(
    token=config('TOKEN'),
    # used to enable slash commands on discord
    default_enabled_guilds=974573532312924160
)


# Log status of bot
@bot.listen(hikari.StartedEvent)
async def on_start(event):
    print('Bot started')


# Define Datastore on startup
@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()


# delete datastore on shutdown
@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    await bot.d.aio_session.close()


# Error handling
@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(
            f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")


bot.load_extensions_from("./extensions", must_exist=True, recursive=True)

# run the bot   
bot.run()
