import discord
from discord import colour
from discord.embeds import Embed
from discord.ext import commands
import os
from discord.ext.commands.core import command
from discord.ext.commands.errors import MissingRequiredArgument, UserInputError
from discord.user import User
import discord.utils
import random
import time
import datetime

fake_emails = random.choice(['@alienAss.com', '@JumboButt.com','@fishyLegs.com', '@FreakSchool.com', '@KillerAss.com', '@stfu.com'])

common_words = random.choice(['Cool', 'Amazing', 'Language', 'Dumbshit', 'Idiot', 'Meme', 'a', 'e', 'i', 'o', 'u'])

fake_pass = random.choice(['nothingmuch', 'dumbPersonIam', '*****', 'IamAnIdiot', '12345', 'password'])

best_fake_friends = random.choice(['Censor', 'I am Dumb Like you', 'The guy he hates the most', 'The biggest ass', 'no one'])

roasts = random.choice(['Oh you’re talking to me, I thought you only talked behind my back',
                        "Don’t you get tired of putting make up on two faces every morning?",
                        "Too bad you can’t count jumping to conclusions and running your mouth as exercise."
                        "Is your drama going to an intermission soon?",
                        "My business is my business. Unless you’re a thong, get out of my ass.",
                        "It’s a shame you can’t Photoshop your personality.",
                        "I don’t sugarcoat shit. I’m not Willy Wonka.",
                        "Calm down. Take a deep breath and then hold it for about twenty minutes.",
                        "When karma comes back to punch you in the face, I want to be there in case it needs help.",
                        "You have more faces than Mount Rushmore",
                        "Where’s your off button?",
                        "If I had a face like yours I’d sue my parents.",
                        "I’m jealous of people who don’t know you.",
                        "Is there an app I can download to make you disappear?",
                        "It’s scary to think people like you are allowed to vote. ",
                        "I’m sorry, what language are you speaking? It sounds like bullshit.",
                        "I keep thinking you can’t get any dumber and you keep proving me wrong."])

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lmgtfy'], help="Search the google for your query!? Amazing man!", usage="`#google (whatever you wanna google!)`")
    async def google(self, ctx, term=None):
        if term != None:
            link = f"http://lmgtfy.com/?q={term}"
            em = discord.Embed(title="LMGTFY", url=f"http://lmgtfy.com/?q={term}", description="Use the above link and find whatever you asked me for! Can't help more than this! Lazy a**", colour=discord.Colour.magenta())
            await ctx.reply(link, embed=em)
        elif term == None:
            await ctx.reply("You have to send what you want to search on google with the command!")


    @commands.command(aliases=['howchump', 'chumpness'], help="Use this command to check how much a chimp you are you can also mention someone to check how chimp they are", usage="`#chumprate`")
    async def chumprate(self, ctx, member: discord.Member = None):
        if member == None:
            chimpness = random.randrange(1, 100)
            embed = discord.Embed(title='Chimp_Rate Machine', description=f"You are {chimpness}% chump", colour=discord.Colour.teal())
            await ctx.send(embed=embed)
        elif member != None:
            chimpness = random.randrange(1, 100)
            embed = discord.Embed(title="Chimp_Rate Machine", description=f"{member.name}, is {chimpness}% chump", colour=discord.Colour.blue())
            await ctx.send(embed=embed)

    @commands.command(aliases=['dumbweb'], help="Go and check a website which is completely useless? You will enjoy it tho!", usage="`#uselessweb`")
    async def uselessweb(self, ctx):
        links = random.choice(['https://mondrianandme.com/', 'https://thatsthefinger.com/', 'http://endless.horse/', 'http://eelslap.com/', 'https://smashthewalls.com/', 'https://alwaysjudgeabookbyitscover.com/','https://weirdorconfusing.com/', 'https://cant-not-tweet-this.com/', 'https://trypap.com/', 'https://jacksonpollock.org/', 'https://heeeeeeeey.com/', 'http://burymewithmymoney.com/', 'http://www.movenowthinklater.com/', 'http://www.everydayim.com/', 'https://cat-bounce.com/', 'https://chrismckenzie.com/', 'https://thezen.zone/'])
        await ctx.reply(links) 

    @commands.command(aliases=['gamerrate', 'epicgamerrate'], help="Check how much a gamer you are!?", usage="`#howgamer`")
    async def howgamer(self, ctx, member: discord.Member = None):
        gamerrate = random.randrange(1, 100)
        if member == None:
            embed = discord.Embed(title="HowGamer", description=f"You are {gamerrate}% gamer", colour=discord.Colour.teal())
            await ctx.send(embed=embed)
        elif member != None:
            embed = discord.Embed(title="HowGamer", description=f"{member.name} is {gamerrate}% gamer", colour=discord.Colour.teal())
            await ctx.send(embed=embed)

    @commands.command(aliases=["howsimp", "simpness"], help="Use the command to check how much of a simp you are mention someone to see how much of a simp they too are!", usage="`#simprate`")
    async def simprate(self, ctx, member: discord.Member=None):
        simpness = random.randrange(1, 100)
        if member == None:
            embed = discord.Embed(title="HowSimp", description=f"You are {simpness}% simp", colour=discord.Colour.teal())
            await ctx.send(embed=embed)
        elif member != None:
            embed = discord.Embed(title="HowSimp", description=f"{member.name} is {simpness}% simp", colour=discord.Colour.teal())
            await ctx.send(embed=embed)

    @commands.command(aliases=["tease"], help="Use the command to roast someone just by mentioning them", usage="`#roast (@member)`")
    async def roast(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.reply("Hey you gotta mention the person you wanna roast with your command **or else what, Should I roast you**")
        elif member != None:
            await ctx.send(roasts)

    @commands.command(aliases=['cybercrime'], help="Use the command to hack someone by mentioning them!", usage="`#hack (@member)`")
    async def hack(self, ctx, member: discord.Member = None):
        if member != None:
            msg1 = await ctx.send(f"Hacking {member} now...")
            time.sleep(2)
            await msg1.edit(content="Finding his discord login **(2FA Has been cleared)**")
            time.sleep(2)
            await msg1.edit(content=f"**Found:** \n```email: {member}{fake_emails}``` ```password: {fake_pass}```")
            time.sleep(2)
            await msg1.edit(content="Finding his most common word in chats")
            time.sleep(3)
            await msg1.edit(content=f"**Found his most common word: {common_words}**")
            time.sleep(2)
            await msg1.edit(content=f"Finding his best friends name on discord! **If there is any friend!??**")
            time.sleep(1)
            await msg1.edit(content=f"Found his best friend, its **{best_fake_friends}**")
            time.sleep(3)
            await msg1.edit(content=f"Hacking {member.name}'s medical records **now...**")
            time.sleep(3)
            await msg1.edit(content=f"Selling all his message history on the **dark net!**")
            time.sleep(2)
            await msg1.edit(content=f"I have finished hacking {member}")
            await ctx.send("It was one of the most **dangerous** hacks ever")
        else:
            await ctx.send(f"Hey! {ctx.author.mention}, you have to mention someone to hack!")


    @commands.command(help="Use the command to check how much of a gay you are or mention someone to check howgay they are!?", usage="`#howgay`", aliases=['gayness'])
    async def howgay(self, ctx, member: discord.Member=None):
        gayness = random.randrange(1, 100)
        if member == None:
            self_embed = discord.Embed(title="Gay Rate Machine", description=f"{ctx.author.name} is {gayness}% gay!", colour=discord.Colour.green())
            await ctx.send(embed=self_embed)
        elif member != None:
            mem_embed = discord.Embed(title="Gay Rate Machine", description=f"{member} is {gayness}% gay!", colour=discord.Colour.teal())
            await ctx.send(embed=mem_embed)


    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Don’t count on it.',
                    'It is certain.',
                    'It is decidedly so.',
                    'Most likely.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Outlook good.',
                    'Reply hazy, try again.',
                    'Signs point to yes.',
                    'Very doubtful.',
                    'Without a doubt.',
                    'Yes.',
                    'Yes – definitely.',
                    'You may rely on it.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(help="Use the command to tell me a spoiler! Shhh! I won't tell it to anyone", usage="`#spoiler (spoiler stuff)`", aliases=['secret'])
    async def spoiler(self, ctx, string: str=None):
        if string == None:
            await ctx.reply("Hey you have to tell me what is the spoiler")
        elif string != None:
            await ctx.send(f"|| {string} ||")


    

def setup(bot):
    bot.add_cog(Fun(bot))
