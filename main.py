#import
import discord
from discord import colour
from discord import message
from discord.ext import commands
import os
from discord.ext.commands.core import command, cooldown
import discord.utils
import random
from discord.ext.commands import BucketType


#Bot instance
bot = commands.Bot(command_prefix='#')

#Help Command for The bot!
class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.clean_prefix, command.qualified_name, command.signature)
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title=f"{bot.user.name}'s Help", colour=discord.Colour.red())
        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [self.get_command_signature(c) for c in filtered]
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)
        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=f"__#{command} help__", colour=discord.Colour.teal())
        embed.add_field(name="**Description**", value=command.help)
        alias = command.aliases
        usage = command.usage
        if alias:
            embed.add_field(name="**Aliases**", value=", ".join(alias), inline=False)
        if alias == None:
            embed.add_field(name="**Aliases**", value="None", inline=False)
        if usage:
            embed.add_field(name="**Usage**", value=usage, inline=False)
        embed.set_footer(text="Please use # before each command!")
        channel = self.get_destination()
        await channel.send(embed=embed)

bot.help_command = MyHelp()

#Loading the cogs
bot.load_extension(f"cogs.currency")
bot.load_extension(f"cogs.functions")
bot.load_extension(f"cogs.games")
bot.load_extension(f"cogs.fun") 


bot.run(os.environ(BOT_TOKEN))
