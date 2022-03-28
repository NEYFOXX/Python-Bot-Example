import nextcord
from nextcord.ext import commands

class LockUnlock(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.command(brief="Permet de bloquer le salon aux membres")
    async def lock(self, ctx, *, reason = "Aucune raison fournie"):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
        await ctx.send(f"Le salon a bien été lock")
    
    @commands.command(brief="Permet de débloquer le salon aux membres")
    async def unlock(self, ctx, *, reason = "Aucune raison fournie"):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
        await ctx.send(f"Le salon a bien été débloqué")

def setup(bot):
    bot.add_cog(LockUnlock(bot))