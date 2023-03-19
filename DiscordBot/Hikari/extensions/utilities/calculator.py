import lightbulb

calculator_plugin = lightbulb.Plugin('translate', 'this translates your text')


# Init the Group to handle the commands for calculation
@calculator_plugin.command()
@lightbulb.command('calculator', 'This will group all calculator commands')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calculator(ctx):
    pass


# Init the Group to handle the command for Addition of 2 numbers
@calculator.child
@lightbulb.option('number2', 'Second number', type=int)
@lightbulb.option('number1', 'First number', type=int)
@lightbulb.command('add', 'this is adds two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def add(ctx):
    await ctx.respond('Sum: ' + str(ctx.options['number1'] + ctx.options['number2']))


# Init the Group to handle the command for Subtraction of 2 numbers
@calculator.child
@lightbulb.option('number2', 'Second number', type=int)
@lightbulb.option('number1', 'First number', type=int)
@lightbulb.command('subtract', 'this is subtracts two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def add(ctx):
    await ctx.respond('Difference: ' + str(ctx.options['number1'] - ctx.options['number2']))


# Init the Group to handle the command for Multiplication of 2 numbers
@calculator.child
@lightbulb.option('number2', 'Second number', type=int)
@lightbulb.option('number1', 'First number', type=int)
@lightbulb.command('multiply', 'this is multiplies two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def add(ctx):
    await ctx.respond('Product: ' + str(ctx.options['number1'] * ctx.options['number2']))


# Init the Group to handle the command for Division of 2 numbers
@calculator.child
@lightbulb.option('number2', 'Second number', type=float)
@lightbulb.option('number1', 'First number', type=float)
@lightbulb.command('divide', 'this is divides two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def add(ctx):
    await ctx.respond('Quotient: ' + str(ctx.options['number1'] / ctx.options['number2']))


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(calculator_plugin)
