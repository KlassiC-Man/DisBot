import discord
from discord import colour
from discord.ext import commands
import os
import random
import json
from discord.ext.commands import BucketType
from discord.ext.commands.core import command, cooldown
import datetime

async def open_account(user):
  users = await get_bank_data()
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 0
    users[str(user.id)]["bank"] = 0
  with open("usersbank.json", "w") as f:
    json.dump(users, f)
  return True


async def get_bank_data():
    with open("usersbank.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("usersbank.json", "w") as f:
        json.dump(users, f)
    bal = users[str(user.id)]["wallet"], users[str(user.id)]["bank"]
    return bal


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break
    if name_ == None:
        return [False, 1]
    cost = price*amount
    users = await get_bank_data()
    bal = await update_bank(user)
    if bal[0] < cost:
        return [False, 2]
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]
    with open("usersbank.json", "w") as f:
        json.dump(users, f)
    await update_bank(user, cost*-1, "wallet")
    return [True, "Worked"]


async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.9 * item["price"]
            break
    if name_ == None:
        return [False, 1]
    cost = price*amount
    users = await get_bank_data()
    bal = await update_bank(user)
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]
    with open("usersbank.json", "w") as f:
        json.dump(users, f)
    await update_bank(user, cost, "wallet")
    return [True, "Worked"]


mainshop = [{"name": "watch", "price": 2400, "description": "Show off your watch to all!, However its just useless"},
            {"name": "Fishing_Rod", "price": 1700,
             "description": "Helps you in fishing you can use the #fish command if you have a fishing rod!"},
            {"name": "Second_Hand_Laptop", "price": 2500,
             "description": "Just a second hand laptop which might be in your budget"},
            {"name": "Fidget_Spinner", "price": 1000,
             "description": "Spin it the fastest you can!"},
            {"name": "Mobile_Phone", "price": 2700,
             "description": "Just an amazing mobile phone but who cares its just for show off"},
            {"name": "Bag_Lock", "price": 2000, "description": "Nobody can rob you if you have even one of these"}]


class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help="Beg some money from the bot so that you are not poor anymore! Sometimes you may get a good amount of money sometimes you may not get even a single penny!", usage="`#beg`")
    @commands.guild_only()
    @commands.cooldown(1, 45, BucketType.user)
    async def beg(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        earnings = random.randrange(500)
        giver = random.choice(['Thanos', 'Deadpool', 'Han Solo', 'Batman',
                            'The Joker', 'Darth Vader', 'Captain Jack Sparrow'])
        await ctx.send(f"**{giver} gave you {earnings} coins!!**")
        users[str(user.id)]["wallet"] += earnings
        with open("usersbank.json", "w") as f:
            json.dump(users, f)

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error = error.retry_after
            ti = round(error)
            beg_embed = discord.Embed(
                title="Whoa! Whoa! Too Fast!", description=f"{ctx.author.mention} Stop begging so much are you a begger. You can beg later after {ti} seconds....", colour=discord.Colour.dark_red())
            await ctx.send(embed=beg_embed)
        else:
            await ctx.send("An error was caused SORRY!")

    @commands.command(help="Use the command to check what commands are there in your bag!", usage="#bag")
    async def bag(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []
        em = discord.Embed(title="Bag")
        for item in bag:
            name = item["item"]
            amount = item["amount"]
            em.add_field(name=name, value=amount)
        await ctx.send(embed=em)


    @commands.command(help="Use this command to sell stuff in your bag which you have bought for some money!", usage="#sell (name of item)")
    @commands.guild_only()
    async def sell(self, ctx, item, amount=1):
        await open_account(ctx.author)
        res = await sell_this(ctx.author, item, amount)
        if not res[0]:
            if res[1] == 1:
                await ctx.send("That Object isn't there!")
                return
            if res[1] == 2:
                await ctx.send(f"You don't have {amount} {item} in your bag.")
                return
            if res[1] == 3:
                await ctx.send(f"You don't have {item} in your bag.")
                return
        await ctx.send(f"You just sold {amount} {item}.")

    @commands.command(help=f"Use the command to check the shop and buy some items from there!", usage="`#shop`")
    @commands.guild_only()
    async def shop(self, ctx):
        embed = discord.Embed(
            title=f"**{self.bot.user}'s shop**", colour=discord.Colour.red())
        for item in mainshop:
            name = item["name"]
            price = item["price"]
            description = item["description"]
            embed.add_field(name=f'**{name}--${price}**',
                            value=f'description: {description}', inline=False)
            embed.set_footer(text="To buy something use **#buy 'Thing'**")
        await ctx.send(embed=embed)

    @commands.command(help=f"Use the command to buy something from the shop!", usage="`#buy (Name of thing)`")
    @commands.guild_only()
    async def buy(self, ctx, item, amount=1):
        await open_account(ctx.author)
        res = await buy_this(ctx.author, item, amount)
        if not res[0]:
            if res[1] == 1:
                await ctx.send("**That object isn't there in the list you poop!**")
                return
            if res[1] == 2:
                await ctx.send(f"**That seems to be out of your budget idiot!*USE BALANCE COMMAND TO CHECK HOW MUCH YOUR BUDGET IS!***")
                return
        await ctx.send(f"**Oh you bought {item}, congratulations**")

    @commands.command(aliases=['bal'], help="Use the command to check your wallet or bank balance!", usage="`#balance`")
    async def balance(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        embed = discord.Embed(title=f"{ctx.author.name}'s balance", color=0xFF69B4)
        embed.add_field(name="Wallet Balance", value=wallet_amt, inline=False)
        embed.add_field(name="Bank Balance", value=bank_amt, inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['with'], help="Use the command to withdraw money from your bank account to your wallet balance", usage="`#withdraw`")
    @commands.guild_only()
    async def withdraw(self, ctx, amount=None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("**Please enter the amount**")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("**You dont have that much money!!**")
            return
        if amount < 0:
            await ctx.send("**Amount must be positive**")
            return
        await update_bank(ctx.author, amount)
        await update_bank(ctx.author, -1*amount, "bank")
        await ctx.send(f"**you withdrew {amount} coins!**")

    @commands.command(aliases=['dep'], help=f"Use the command to deposit money in your wallet to your bank account so it remains safe!", usage="`#deposit (amount)`")
    @commands.guild_only()
    async def deposit(self, ctx, amount=None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("**Please enter the amount**")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("**You dont have that much money!!*Such An Idiot!***")
            return
        if amount < 0:
            await ctx.send("**Hey You dumb person the amount must be positive!* I still didnt understand how does negative money work! LOL***")
            return
        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author, amount, "bank")
        await ctx.send(f"**you deposited {amount} coins!**")


    @commands.command(aliases=['gamble'], help="Bet and gamble with the bot for some money! Amazing right?!", usage='`#bet (amount)`')
    @commands.cooldown(1, 10, BucketType.user)
    async def bet(self, ctx, amount=None):
        await open_account(ctx.author)
        users = await get_bank_data()
        user = ctx.author
        multiplier = random.randint(1, 100)
        if amount == None:
            await ctx.send("Please enter the amount you want to bet along with the command")
            return
        bal = await update_bank(ctx.author)
        amount = int(amount)
        if amount > bal[0]:
            await ctx.send(f"Hey! {ctx.author.mention}, You **don't** have that much money in your wallet")
        elif amount < 0:
            await ctx.send(f"Hey {ctx.author.mention}, you **can't** bet negative amounts!")
        elif amount < 50:
            await ctx.send(f"{ctx.author.mention}, you cant bet less than **50**")
        else:
            bot_dice = random.randrange(1, 12)
            user_dice = random.randrange(1, 12)
            if user_dice > bot_dice:
                earning_per = multiplier / 100 * amount
                earning = amount + earning_per
                new_bal = bal[0] + earning
                user_embed = discord.Embed(
                    title=f"{ctx.author}'s winning bet!", colour=discord.Colour.blue())
                user_embed.add_field(name="WON:", value=earning)
                user_embed.add_field(
                    name=f"{self.bot.user} rolled:", value=f"{bot_dice}", inline=False)
                user_embed.add_field(
                    name=f"{ctx.author} rolled:", value=f"{user_dice}", inline=False)
                user_embed.add_field(name="**NEW BALANCE:**",
                                    value=new_bal, inline=False)
                user_embed.set_footer(
                    text=f"Current multiplier is set to: **{multiplier}**")
                user_embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.send(embed=user_embed)
                users[str(user.id)]["wallet"] += earning
                with open("usersbank.json", 'w') as f:
                    json.dump(users, f)
            elif user_dice < bot_dice:
                loosing_per = multiplier / 100 * amount
                loosing_amt = amount - loosing_per
                new_bal_loss = bal[0] - loosing_amt
                bot_embed = discord.Embed(
                    title=f"{ctx.author}'s loosing bet!", colour=discord.Colour.red())
                bot_embed.add_field(name="LOSS:", value=loosing_amt)
                bot_embed.add_field(name=f"{self.bot.user} rolled:",
                                    value=f"{bot_dice}", inline=False)
                bot_embed.add_field(name=f"{ctx.author} rolled:",
                                    value=f"{user_dice}", inline=False)
                bot_embed.add_field(name="**NEW BALANCE:**",
                                    value=new_bal_loss, inline=False)
                bot_embed.set_thumbnail(url=ctx.author.avatar_url)
                bot_embed.set_footer(text=f"Current multiplier set to: **{multiplier}**")
                await ctx.send(embed=bot_embed)
                users[str(user.id)]["wallet"] -= loosing_amt
                with open("usersbank.json", 'w') as f:
                    json.dump(users, f)
            elif user_dice == bot_dice:
                tied_per = multiplier / 100 * amount
                tied_amt = amount - tied_per
                new_bal_tie = bal[0] - tied_per
                tie_embed = discord.Embed(
                    title=f"{ctx.author}'s tied bet", colour=0xfff700)
                tie_embed.add_field(name="LOSS:", value=tied_amt)
                tie_embed.add_field(name=f"{self.bot.user} rolled:",
                                    value=f"{bot_dice}", inline=False)
                tie_embed.add_field(name=f"{ctx.author} rolled:",
                                    value=f"{user_dice}", inline=False)
                tie_embed.add_field(name="**NEW BALANCE:**",
                                    value=new_bal_tie, inline=False)
                tie_embed.set_thumbnail(url=ctx.author.avatar_url)
                tie_embed.set_footer(text=f"Current multiplier is set to: {multiplier}")
                await ctx.send(embed=tie_embed)
                users[str(user.id)]["wallet"] -= tied_amt
                with open("usersbank.json", 'w') as f:
                    json.dump(users, f)


    @bet.error
    async def bet_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error = error.retry_after
            ti = round(error)
            bet_error = discord.Embed(title="Stop Betting and Spamming", description=f"Hey! {ctx.author.mention}, please bet only after {ti} more seconds.")
            bet_error.set_thumbnail(url=ctx.author.avatar_url)
            bet_error.set_footer(text=datetime.datetime.now())
            await ctx.send(embed=bet_error)

    @commands.command(help="Post a meme on social media and see how much money you get for that", aliases=['pm'], usage="`#postmeme`")
    @commands.cooldown(1, 25, BucketType.user)
    async def postmeme(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        await ctx.send(f"{ctx.author.mention}, **__What Type of Meme Do You Want To Post?__**\n``f``: **Fresh Meme**\n``r``: **Reposted Meme**\n``i``: **Intellectual Meme**\n``c``: **Copypasted Meme**\n``k``: **Kind Meme**")
        earning = random.randrange(2000)
        def check(m):
            return m.content == 'f', 'i', 'c', 'r', 'k' and m.channel == ctx.channel
        await self.bot.wait_for('message', check=check, timeout=30)
        if earning < 500:
            await ctx.send(f"You earned a decent response from the internet regarding the meme. So you get **{earning}**")
            users[str(user.id)]["wallet"] += earning
            with open("usersbank.json", 'w') as f:
                json.dump(users, f)
        elif earning < 1000:
            await ctx.send(f"You earned a fairly good response from the internet regarding the meme. So you get **{earning}**")
            users[str(user.id)]["wallet"] += earning
            with open("usersbank.json", 'w') as f:
                json.dump(users, f)
        elif earning < 100:
            await ctx.send(f"You earned a bad enough response from the internet regarding the meme. So you get **{earning}**")
            users[str(user.id)]["wallet"] += earning
            with open("usersbank.json", 'w') as f:
                json.dump(users, f)
        elif earning > 1500:
            await ctx.send(f"You earned an amazing response from the internet regarding the meme. So you get **{earning}**")
            users[str(user.id)]["wallet"] += earning
            with open("usersbank.json", 'w') as f:
                json.dump(users, f)
        elif earning > 1000:
            await ctx.send(f"You earned a very good resposne from the internet regarding the meme. So you get **{earning}**")
            users[str(user.id)]["wallet"] += earning
            with open("usersbank.json", 'w') as f:
                json.dump(users, f)

    
    @postmeme.error
    async def postmeme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            error = error.retry_after
            tim = round(error)
            embed = discord.Embed(title="Tooo Fast Man!", description=f"You can post meme after {tim} more seconds")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.reply(embed=embed, mention_author=True)



def setup(bot):
    bot.add_cog(Currency(bot))
