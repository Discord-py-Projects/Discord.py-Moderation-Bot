import discord
import os
from discord.ext import commands

TOKEN = "ODU1NTAwMDg0OTUwNTk3NjMz.YMzYig.S5PVSFGTueVnEOrIpeJCfTkd33c"
PREFIX = "."

bot = commands.AutoShardedBot(command_prefix=PREFIX)
bot.remove_command('help')

@bot.event
async def on_ready():
	print('Bot is ready')
	activity = discord.Activity(type=discord.ActivityType.listening, name=F"{PREFIX}help")
	await bot.change_presence(status=discord.Status.dnd, activity=activity)


for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")

bot.run(TOKEN)