import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix='/', help_command=None, intents=disnake.Intents.all())
CENSORED_WORDS = ["Пизда", "Сука", "Блять", "Пидорас", 'пизда', 'сука', 'блять', 'пидорас']


@bot.event
async def on_ready():
    print(f'{bot.user}, он же работяга Chak, готов ебашить смену')


@bot.event
async def on_message(message):
    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content == censored_word:
                await message.delete()
                await message.channel.send(f'{message.author.mention} ахуел?')



























bot.run('MTA4NDQ0MTc2NzU4MTA2OTM3NA.Ga6n5-.5lz4oA8gWo2cqZnwrv8xxbPBXoStOm2Y6r6xnc')