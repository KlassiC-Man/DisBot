import discord
from discord.ext import commands
import os
from cogs.currency import Currency


class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Hello I am ready!")
        


def setup(bot):
    bot.add_cog(Functions(bot))
