import discord
from discord.ext import commands
import json
import keep_alive

bot1 = commands.Bot(command_prefix='?')

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

@bot1.event
async def on_ready():
  print(">> Bot is online <<")

@bot1.event
async def on_member_join(member):
	channel = bot.get_channel(int(jdata['we']))
	await channel.send(f'{member} join')

@bot1.event
async def on_member_remove(member):
	channel = bot.get_channel(int(jdata['le']))
	await channel.send(f'{member} leave')

@bot1.command()
async def ping(ctx):
  await ctx.send(f'{bot.latency*1000} (ms)')

@bot1.command()
async def hi(ctx):
  await ctx.send(hi)

@bot1.command()
async def web(ctx):
	random_pic = ramdom.choice()


keep_alive.keep_alive()
bot1.run(jdata['TOKEN'])
