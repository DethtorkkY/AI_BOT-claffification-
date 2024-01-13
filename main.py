import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = 'MTEzMjI3Nzk1NzQ5OTU3MjMxNA.G7vX3A.V8OxIVXzsWo_93H6uo8LOHHTVnCmyY6uVOVEdc'

# команды
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            fiele_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(image=f'./{attachment.filename}', model="keras_model.h5" , labels="labels.txt"))
    else:
        await ctx.send("вы забыли прикрепить картинку:(")

bot.run(TOKEN)
