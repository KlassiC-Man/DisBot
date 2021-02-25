import discord
import json
from discord.ext import commands
import os

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['cutomprefix'], help="Use the command to change the prefix", usage="`#customprefix`")
    async def changeprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send("Prefix successfully changed!")


def setup(bot):
    bot.add_cog(Utility(bot))
