from re import X
import discord
from discord import player
from discord.ext import commands
import os
import random

from discord.ext.commands.core import check, command, cooldown


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Play rock paper scizzor with the bot! Lets see if you win!? **Note: This command doesnt include money!**", usage="`#rps (rock, paper or scizzor)`")
    @commands.bot_has_permissions(send_messages=True, embed_links=True)
    async def rps(self, ctx, user_choice):
        bot_choice = random.choice(['rock', 'paper', 'scizzor'])
        if bot_choice == 'rock':
            if user_choice == 'paper':
                em = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game", colour=discord.Colour.green())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:", value='paper', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif user_choice == 'rock':
                em = discord.Embed(title=f"{ctx.author.name}'s Tied RPS Game!", colour=discord.Colour.gold())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:", value='rock', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif user_choice == 'scizzor':
                em = discord.Embed(title=f"{ctx.author.name}'s Loosing RPS Game!", colour=discord.Colour.red())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:", value='scizzor', inline=False)             
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
        elif bot_choice == 'scizzor':
            if user_choice == 'paper':
                em = discord.Embed(title=f"{ctx.author.name}'s Loosing RPS Game!", colour=discord.Colour.red())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:",value='paper', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif user_choice == 'scizzor':
                em = discord.Embed(title=f"{ctx.author.name}'s Tied RPS Game", colour=discord.Colour.gold())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:",value='scizzor', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif user_choice == 'rock':
                em = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game", colour=discord.Colour.green())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:",value='rock', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
        elif bot_choice == 'paper':
            if user_choice == 'paper':
                em = discord.Embed(title=f"{ctx.author.name}'s Tied RPS Game", colour=discord.Colour.gold())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:",value='paper', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif user_choice == 'scizzor':
                em = discord.Embed(title=f"{ctx.author.name}'s Winning RPS Game", colour=discord.Colour.green())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:",value='scizzor', inline=False)
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)
            elif user_choice == 'rock':
                em = discord.Embed(title=f"{ctx.author.name}'s Loosing RPS Game", colour=discord.Colour.red())
                em.add_field(name="Bot played:", value=bot_choice, inline=False)
                em.add_field(name=f"{ctx.author.name} played:", value='rock')
                em.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(Games(bot))
