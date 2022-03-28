import nextcord
from nextcord.ext import commands
from nextcord import guild

class Ban(commands.Cog):
    def __init__(self, bot):
            self.bot = bot
    
    @commands.command(aliases=["b"], brief="Bannir un utilisateur de votre serveur")
    async def ban(self, ctx, member: nextcord.Member, *, reason="Aucune raison fournie"):
        print('cmd prise en compte')
        if member.id == ctx.author.id:
            return await ctx.send("Vous ne pouvez pas vous bannir vous-même")
        print('if bypassed')
        embed = nextcord.Embed(title="Ban", description=f'Bannissement : {member.mention}\nRaison : {reason}')
        await ctx.send(embed=embed)
        print('embed envoyé')
        await member.ban(reason=reason)
        print('ban effectué')
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Mauvaise utilisation, faites `+ban <user> [raison]`')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'Je n\'ai pas les permissions suffisantes pour pouvoir bannir un membre')

def setup(bot):
    bot.add_cog(Ban(bot))