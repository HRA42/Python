import lightbulb
import deepl  # get translations from deepl
from decouple import config  # read env variables for token

translation_plugin = lightbulb.Plugin('translate', 'this translates your text')

# Init Deepl Translator API
auth_key = config('DEEPL-API-KEY')
deep_translator = deepl.Translator(auth_key)
# create empty list
target_lang = []
# create a list with name plus language code
for language in deep_translator.get_target_languages():
    target_lang = target_lang + [language.name + " - " + language.code]
# discord only allows 25 options, so we need the short the list to the first 25 entries at runtime
target_lang = target_lang[0:25]


@translation_plugin.command()
@lightbulb.option('text', 'Input your Source Text here', type=str)
@lightbulb.option(
    # Define a target language with the options from the top target languages list
    name='target',
    description='Input your Target Language here',
    choices=target_lang,
    required=True,
    type=str
)
@lightbulb.command('translate', 'this translates your text')
@lightbulb.implements(lightbulb.SlashCommand)
async def translator(ctx):
    await ctx.respond(
        # DeepL API requires you to provide only a language code, so we need to extract that
        # Use the definied " - " between them for the split and return the language code
        deep_translator.translate_text(ctx.options['text'], target_lang=ctx.options['target'].split(' - ')[1])
    )


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(translation_plugin)
