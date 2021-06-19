import discord
import datetime
from discord.ext import commands
import bot

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help(self, ctx):
		embed = discord.Embed(title="Help!", description="How to use the commands!", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.blue())
		embed.add_field(name=f"{bot.PREFIX}ping", value="This command is too show the latency of the bot", inline=True)
		embed.add_field(name=f"{bot.PREFIX}purge", value=f"Syntax: {bot.PREFIX}purge (amount of messages), This command is too delete certant amount of messages in a channel!", inline=True)
		embed.add_field(name=f"{bot.PREFIX}tempmute", value=f"Syntax: {bot.PREFIX}tempmute (member) (time) (time delay(example: s, m, h, d)) (reason), This command is to temperaly mute a member!", inline=True)
		embed.add_field(name=f"{bot.PREFIX}mute", value=f"Syntax: {bot.PREFIX}mute (member) (reason), This command is to permentaly mute a member untill unmuted with a command", inline=True)
		embed.add_field(name=f"{bot.PREFIX}unmute", value=f"Syntax: {bot.PREFIX}unmute (member), This command is to unmute a member forcefully", inline=True)
		embed.add_field(name=f"{bot.PREFIX}kick", value=f"Syntax: {bot.PREFIX}kick (member) (reason, This command is to kick a member from you're guild! They still can rejoin if given an invite)", inline=True)
		embed.add_field(name=f"{bot.PREFIX}tempban", value=f"Syntax: {bot.PREFIX}tempban (member) (time) (time delay(example: s, m, h, d)) (reason), This command is to temperaly ban a member untill time is up or unban command is called on the member", inline=True)
		embed.add_field(name=f"{bot.PREFIX}ban", value=f"Syntax: {bot.PREFIX}ban (member) (reason), This command is to permentaly mute a member untill unbannedd with a command", inline=True)
		embed.add_field(name=f"{bot.PREFIX}unban", value=f"Syntax: {bot.PREFIX}unban (member), This command is to unban a member forcefully", inline=True)
		await ctx.reply(embed=embed)

def setup(bot):
	bot.add_cog(Help(bot))