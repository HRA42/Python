# Discord Bot

## Check out the Page on [Dockerhub](https://hub.docker.com/r/dnshra/discordbot)

You should use the docker images provided because they make clean environments for testing out the bot.

Just run the image and when you are done you can stop and remove the container, without affecting the host system.

[Learn more about Docker](https://docs.docker.com/get-started/overview/)
## Discord.Py API Reference

[Learn more about Discord API](https://discordpy.readthedocs.io/en/stable/api.html)

### Use the Discord.Py Image on Dockerhub

```bash
docker run -e "TOKEN=YOUR_DISCORD_TOKEN" dnshra/discordbot:discord.py
```

[Dockerhub Discord.PY Image](https://hub.docker.com/layers/discordbot/dnshra/discordbot/discord.py/images/sha256-1bd54f4c2dab366ca9d8180bfbec19c9051aed63324f9e94ec2de81afab5a6a3?context=explore)


```
Tip!
You can also use the commands in the Dockerfile to install the discord bot to your hardware.
```

### Features

This bot has the ability to calculate the basic math functions and return them to the user.

| Command | Function |
|:-:|:-:|
| !addition | Adds 2 numbers together |
| !subtraction | Subtracts 2 numbers |
| !multiplication | Multiplies 2 numbers |
| !division | Divide 2 numbers |


---

## Hikari API Reference

I like to use Hikari because it's super easy to implement slash commands, so I don’t need to remember what commands I already implemented. 

Between starting and finishing this project discord.py got discontinued and then continued working on so in my opinion it's not stable enough to provide a long-term API Wrapper for Discord.

[Learn more about Hikari API](https://www.hikari-py.dev/hikari/index.html)

[Learn more about Hikari-Lightbulb Eventhandler API](https://hikari-lightbulb.readthedocs.io/en/latest/)

### Use the Hikari Image on Dockerhub

```bash
docker run -e "DEEPL-API-KEY=YOUR_DEEPL_KEY" -e "TOKEN=YOUR_DISCORD_TOKEN"  dnshra/discordbot:hikari
```

[Dockerhub Hikari Image](https://hub.docker.com/layers/discordbot/dnshra/discordbot/hikari/images/sha256-82b4171b294623e92fce54ab8efb133d3ddb5f234360d265e23479a263c190c4?context=explore)


```
Tip!
You can also use the commands in the Dockerfile to install the discord bot to your hardware.
```

### Features

This Bot implements different functions organized into categories.

| Command | Function |
|:-:|:-:|
| **Category** | **Fun** |
| /meme | provides a meme from the reddit api |
| **Category** | **Moderation** |
| /purge n | deletes the last n messages from invoking the command |
| **Category** | **Utilities** |
| /translate your_original_text target_language | translates a text to a target language of your choice |
| /calculator add n m | Add 2 numbers together |
| /calculator subtract n m | Subtracts 2 numbers |
| /calculator multiply n m | Multiplies 2 numbers |
| /calculator divide n m | Divides 2 numbers |


```
WARNING!
The translation command requires an API Key from DeepL
Check DeepL API reference: <https://www.deepl.com/docs-api>
```