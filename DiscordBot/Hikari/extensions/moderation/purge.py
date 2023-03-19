import lightbulb
import asyncio  # used to sleep for a few seconds

# Enable Plugin for the main bot.py script
purge_plugin = lightbulb.Plugin("purge", "Purge messages.")


# Implement the plugin command
@purge_plugin.command()
# Cooldown for 10 sec after one use, to avoid api missus-age (avoid black listing)
@lightbulb.add_cooldown(10, 1, lightbulb.UserBucket)
@lightbulb.option("messages", "The number of messages to purge.", type=int, required=True)
@lightbulb.command("purge", "Purge messages.", aliases=["clear"])
@lightbulb.implements(lightbulb.SlashCommand)
async def purge_messages(ctx: lightbulb.Context) -> None:
    num_msgs = ctx.options.messages
    channel = ctx.channel_id  # get channel id from command invocation
    msgs = await ctx.bot.rest.fetch_messages(channel).limit(num_msgs)
    await ctx.bot.rest.delete_messages(channel, msgs)
    resp = await ctx.respond(f"{len(msgs)} messages deleted")
    # wait for 5 seconds before deleting the command invocation message
    await asyncio.sleep(5)
    await resp.delete()  # delete the response message


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(purge_plugin)
