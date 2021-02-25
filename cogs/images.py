import discord
from discord.ext import commands
import os
import random
from discord.ext.commands.core import command
import praw

reddit = praw.Reddit(client_id="5-_GzjyTOOhukQ",
                     client_secret=os.environ['REDDIT_SECRET'],
                     username="idioticspaceman",
                     password=os.environ['REDDIT_PASS'])

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Use the command to get a meme", usage="`#meme`", aliases=['memes'])
    async def meme(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit("memes")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            meme_embed = discord.Embed(title=name, colour=discord.Colour.blue())
            meme_embed.set_image(url=url)
            await ctx.send(embed=meme_embed)

    @commands.command(aliases=['dogs'])
    async def dog(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit("dogs")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            dog_embed = discord.Embed(title=name, colour=discord.Colour.teal())
            dog_embed.set_image(url=url)
            await ctx.send(embed=dog_embed)



def setup(bot):
    bot.add_cog(Images(bot))
