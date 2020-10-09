import discord
from discord.ext import commands

TOKEN = open('token.txt','r').readline()
client = commands.Bot(command_prefix = '.')

#answers with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    print('test')

print('Started!')

client.run(TOKEN)