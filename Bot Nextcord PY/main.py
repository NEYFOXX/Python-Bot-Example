from distutils.command import config
import nextcord
from nextcord.ext import commands
import os
import config

bot = commands.Bot(command_prefix=f'+', description="Ceci est un bot pour tester la librairie nextcord")

@bot.event
async def on_ready():
    print(f"Je suis connecté sur {bot.user.display_name}")
    await bot.change_presence(activity=nextcord.Streaming(name="Tohsaka Bots", url="https://twitch.tv/NEYFOXX"))

@bot.command()
async def say(ctx, *args):
    await ctx.message.delete()
    await ctx.send(" ".join(args))

@bot.command()
async def add(ctx, right: int, left: int):
    await ctx.send(right + left)

@bot.command()
async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}')
        await ctx.send('Les extensions ont étés chargés')

@bot.command()
async def unload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Les extensions ont étés chargés : `{extension}`.')

if __name__ == "__main__":
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and not filename.startswith('_'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config.TOKEN)