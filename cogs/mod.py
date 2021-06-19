import discord
import os
import datetime
import asyncio
from discord.ext import commands


class Mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def ping(self, ctx):
		embed = discord.Embed(title=f"🏓Pong! {round(self.bot.latency * 1000)}ms", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def purge(self, ctx, amount=6):
		await ctx.channel.purge(limit=amount)
		embed = discord.Embed(title=f"{amount} messages has been purged!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def tempmute(self, ctx, member: discord.Member, time, d, reason=None):
	    guild = ctx.guild
	    role = discord.utils.get(guild.roles, name="Muted")
	    


	        
	    for channel in guild.channels:
	    	await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=False)
	    await member.add_roles(role)
	    embed = discord.Embed(title="Muted!", description=f"{member.mention} has been muted", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
	    embed.add_field(name="Reason:", value=reason, inline=False)
	    embed.add_field(name="Time left for the mute:", value=f"{time}{d}", inline=False)
	    await ctx.reply(embed=embed)
	    if d == "s":
	    	await asyncio.sleep(int(time))
	    if d == "m":								
	    	await asyncio.sleep(int(time*60))
	    if d == "h":
	    	await asyncio.sleep(int(time*60*60))
	    if d == "d":
	    	await asyncio.sleep(int(time*60*60*24))
	    await member.remove_roles(role)
	    embed = discord.Embed(title="Unmuted", description=f"Unmuted {member.mention} ", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
	    await ctx.reply(embed=embed)

	            
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def mute(self, ctx, member: discord.Member, *, reason=None):
	    guild = ctx.guild
	    mutedRole = discord.utils.get(guild.roles, name="Muted")

	    if not mutedRole:
	        mutedRole = await guild.create_role(name="Muted")

	        for channel in guild.channels:
	            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
	    embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
	    embed.add_field(name="Reason:", value=reason, inline=False)
	    await ctx.reply(embed=embed)
	    await member.add_roles(mutedRole, reason=reason)
	    await member.send(f"You have been muted from: {guild.name} Reason: {reason}")


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member):
	    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	    await member.remove_roles(mutedRole)
	    await member.send(f"You have unmuted from: {ctx.guild.name}")
	    embed = discord.Embed(title="Unmute", description=f"Unmuted {member.mention}", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
	    await ctx.reply(embed=embed)

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def kick(self, ctx, member: discord.Member, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Kicked!", description=f"{member.mention} has been kicked!!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.kick(user=member)

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def tempban(self, ctx, member: discord.Member, time, d, *, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)
			

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Banned!", description=f"{member.mention} has been banned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			embed.add_field(name="Time left for the ban:", value=f"{time}{d}", inline=False)
			await ctx.reply(embed=embed)
			await guild.ban(user=member)

			if d == "s":
				await asyncio.sleep(int(time))
				await guild.unban(user=member)
			if d == "m":
				await asyncio.sleep(int(time*60))
				await guild.unban(user=member)
			if d == "h":
				await asyncio.sleep(int(time*60*60))
				await guild.unban(user=member)
			if d == "d":
				await asyncio.sleep(time*60*60*24)
				await guild.unban(int(user=member))

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def ban(self, ctx, member: discord.Member, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)
		else:
			guild = ctx.guild
			embed = discord.Embed(title="Banned!", description=f"{member.mention} has been banned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.ban(user=member)



	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def unban(self, ctx, user: discord.User):
		if user == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Unbanned!", description=f"{user.display_name} has been unbanned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			await ctx.reply(embed=embed)
			await guild.unban(user=user)



def setup(bot):
	bot.add_cog(Mod(bot))