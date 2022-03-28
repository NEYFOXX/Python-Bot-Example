import nextcord
from nextcord.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Permet d'effacer un certains nombre de message dans le salon du message")
    async def clear(self, ctx, amount: int):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
    
    @clear.error
    async def clear_error(self, ctx, error): 
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Mauvaise utilisation, faites `+clear <nombre>`")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Je ne peux pas supprimer de message")

def setup(bot):
    bot.add_cog(Clear(bot))