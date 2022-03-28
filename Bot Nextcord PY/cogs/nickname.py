import nextcord
from nextcord.ext import commands

class Nickname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["nick"], brief="Changer le nom d'un utilisateur sur le serveur")
    async def nickname(self, ctx, member : nextcord.Member, *, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Le nom de {member.mention} a bien été changé par **{nick}**')

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Mauvaise utilisation, faites `+nickname <nickname> <user>`")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Je ne possède pas assez de permission(s)")

def setup(bot):
    bot.add_cog(Nickname(bot))