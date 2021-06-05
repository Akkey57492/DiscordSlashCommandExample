# Module import
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from discord_slash import SlashCommand, SlashContext
# Module import

bot = commands.Bot(command_prefix="", intents=discord.Intents.all()) # Bot setting
slash = SlashCommand(bot, sync_commands=True) # Slash command setting
bot.remove_command("help") # help command remove

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound): # Command Not Found error exception handling
		return
	raise error

# Standard
@slash.slash(name="example1") # Slash command
async def _example1(example1: SlashCommand, arg1): # Slash command & arg
	await example1.send(f"{arg1}")
	await example1.send(f"{arg1}", hidden=True) # Hidden message

# Argment 2
@slash.slash(name="example2")
async def _example2(example2: SlashCommand, arg1, arg2=None):
	if arg2 == None: # arg2 is option
		await example2.send(f"{arg1}")
		await example2.send(f"{arg1}", hidden=True)
	else:
		await example2.send(f"{arg1}")
		await example2.send(f"{arg1}", hidden=True)
		await example2.send(f"{arg2}")
		await example2.send(f"{arg2}", hidden=True)

bot.run("") # token