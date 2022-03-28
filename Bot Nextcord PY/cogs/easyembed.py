import nextcord
from nextcord.ext import commands


class EasyEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Créer un embed rapidement")
    async def easyembed(self, ctx, title, *, desc):
        embed = nextcord.Embed(title=f'{title}', description=f'{desc}')
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(EasyEmbed(bot))