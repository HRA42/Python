import hikari
import lightbulb

# Enable Plugin for the main bot.py script
meme_plugin = lightbulb.Plugin("meme", "Post a meme")


# Implement the plugin command
@meme_plugin.command()
# Cooldown for 10 sec after one use, to avoid api missus-age (avoid black listing)
@lightbulb.add_cooldown(10, 1, lightbulb.UserBucket)
# output on user
@lightbulb.command("meme", "Post a meme", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def meme(ctx: lightbulb.Context) -> None:
    # Create a session and store the data in the global data store
    async with ctx.bot.d.aio_session.get(
            "https://meme-api.herokuapp.com/gimme"
    ) as response:
        # wait until you get a response in case of high workload
        res = await response.json()

        # check if nsfw content is fetched 
        if response.ok and res["nsfw"] != True:
            link = res["postLink"]
            title = res["title"]
            img_url = res["url"]
            # post the image with provided description and link it to original post
            embed = hikari.Embed(colour=0x3B9DFF)
            embed.set_author(name=title, url=link)
            embed.set_image(img_url)
            # send the meme to discord
            await ctx.respond(embed)
        # in case the response isn't okay or the content fetched it tagged with nsfw respond with error
        else:
            await ctx.respond(
                "Could not fetch a meme :c", flags=hikari.MessageFlag.EPHEMERAL)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(meme_plugin)
