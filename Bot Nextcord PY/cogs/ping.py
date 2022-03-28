import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["latency", "speed"], brief="Voir la latence du bot et de l'api")
    async def ping(self, ctx):
        embed = nextcord.Embed(
            title="Ping",
            description=f"Bot : {int(self.bot.latency * 1000)} ms", 
            color=nextcord.Colour.red()
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Ping(bot))