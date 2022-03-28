import nextcord
from nextcord.ext import commands
import datetime

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Rendre muet un utilisateur")
    async def mute(self, ctx, member : nextcord.Member, *, timereq):
        await member.timeout(timeout=timereq, reason="Timeout")
        await ctx.send(f'{member.mention} **mute** avec succès')

def setup(bot):
    bot.add_cog(Mute(bot))