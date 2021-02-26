import discord
import asyncio
from discord.ext import commands, cooldown
from discord.ext.commands.core import BucketType
from cogs.currency import postmeme, slots


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @postmeme.error
    async def postmeme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error = error.retry_after
            tim = round(error)
            embed = discord.Embed(
                title="Tooo Fast Man!", description=f"You can post meme after {tim} more seconds")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=True)
        elif asyncio.TimeoutError:
            await ctx.send("Ok why the hell did you call me when you didnt want to respond!")
        else:
            await ctx.send("There was an error with the command! **SORRY!**")


    @slots.error
    async def slots_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error = error.retry_after
            tim = round(error)
            embed = discord.Embed(
                title="Tooo Fast Man!", description=f"You can post meme after {tim} more seconds")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=True)
        else:
            await ctx.send("There was an error with the command! **SORRY!**")



def setup(bot):
    bot.add_cog(Errors(bot))
