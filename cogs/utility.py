import discord
from discord.ext import commands
import os


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['export'], help="Use the command to unload categories when required can be done only by server administartor!", usage="`#unload (category)`")
    @commands.is_owner()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
        except Exception as e:
            await ctx.send(f"Couldn't unload the {cog} category")
            return
        await ctx.send("Category unloaded")


    @commands.command(aliases=['import'], help="Use this command to load categories if you have unloaded them **only server owners can use this**", usage="`#load (category)`")
    @commands.is_owner()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(f"cogs.{cog}")
        except Exception as e:
            await ctx.send(f"Couldn't load the category!")
            return
        await ctx.send("Category loaded!")


    @commands.command(aliases=['latency'], help="Use the command to check the bots ping and latency!", usage="`#ping`")
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')



def setup(bot):
    bot.add_cog(Utility(bot))

