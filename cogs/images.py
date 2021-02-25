import discord
from discord.ext import commands
import os
import random
from discord.ext.commands.core import command
import praw

reddit = praw.Reddit(client_id="5-_GzjyTOOhukQ",
                     client_secret=os.environ['REDDIT_SECRET'],
                     username="idioticspaceman",
                     password=os.environ['REDDIT_PASS'],
                     user_agent="Economy-BOT")

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

    @commands.command(aliases=['dogs', 'bark'], help="Use the command to see cute pictures of dogs!", usage="`#dog`")
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

    @commands.command(aliases=['cats', 'meow'], help="Use the command to see cats! MEOWWWW!", usage="`#cat`")
    async def cat(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit("cats")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            cat_embed = discord.Embed(title=name, colour=discord.Colour.teal())
            cat_embed.set_image(url=url)
            await ctx.send(embed=cat_embed)

    @commands.command(aliases=['hoot', 'owls'], help="Use the command to see owls! HOOT HOOT", usage="`#owl`")
    async def owl(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit("owls")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            owl_embed = discord.Embed(title=name, colour=discord.Colour.teal())
            owl_embed.set_image(url=url)
            await ctx.send(embed=owl_embed)

    @commands.command(aliases=['foxxy'], help="Use the command to see foxes", usage="`#fox`")
    async def fox(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit("foxes")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            fox_embed = discord.Embed(title=name, colour=discord.Colour.teal())
            fox_embed.set_image(url=url)
            await ctx.send(embed=fox_embed)
        
    @commands.command(aliases=['lizzards', 'lizzard'], help="Use the command to see a lizzard", usage="`#lizziboi`")
    async def lizziboi(self, ctx):
        async with ctx.typing():
            subreddit = reddit.subreddit("lizards")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)
            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            liz_embed = discord.Embed(title=name, colour=discord.Colour.teal())
            liz_embed.set_image(url=url)
            await ctx.send(embed=liz_embed)



def setup(bot):
    bot.add_cog(Images(bot))
