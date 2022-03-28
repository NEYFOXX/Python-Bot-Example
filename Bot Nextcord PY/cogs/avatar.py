import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import bot

class Avatar(commands.Cog):
    def __init__(self, bot):
            self.bot = bot

    @commands.command(aliases=["pic", "pp"], brief="Donner l'avatar d'un utilisateur")
    async def avatar(self, ctx, *, member : nextcord.Member = None):
        if member == None:
            member = ctx.author
            embed = nextcord.Embed(title=f'{member}')
            embed.set_image(url=member.avatar.url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))