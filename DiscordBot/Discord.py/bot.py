import discord  # discord.py module
from discord.ext import commands  # discord.py module
from decouple import config  # read env variables for token
import sentry_sdk

sentry_sdk.init(
    "https://9b6ee33a6070436f90226f3f97f5809b@o1034905.ingest.sentry.io/6001551",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

bot = commands.Bot(command_prefix='!')  # set listening prefix


@bot.command(name="addition")
async def addition(ctx, arg1, arg2):
    await ctx.send("sum: " + str((float(arg1) + float(arg2))))


@bot.command(name="subtraction")
async def subtraction(ctx, arg1, arg2):
    await ctx.send("difference: " + str((float(arg1) - float(arg2))))


@bot.command(name="multiplication")
async def multiplication(ctx, arg1, arg2):
    await ctx.send("product: " + str((float(arg1) * float(arg2))))


@bot.command(name="division")
async def division(ctx, arg1, arg2):
    await ctx.send("quotient: " + str((float(arg1) / float(arg2))))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


bot.run(config('TOKEN'))
