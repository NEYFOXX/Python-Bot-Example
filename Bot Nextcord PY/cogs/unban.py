import nextcord
from nextcord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["ub"], brief="Révoquer le bannissement d'un utilisateur")
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Membre débanni : {user.name}#{user.discriminator}')
    
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Mauvaise utilisation, faites `+unban <user> [raison]`')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'Je n\'ai pas assez de permission pour pouvoir révoquer le bannissement de cet utilisateur')

def setup(bot):
    bot.add_cog(Unban(bot))