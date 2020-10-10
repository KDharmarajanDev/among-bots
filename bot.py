import os
import database
import discord
from discord.ext import commands

TOKEN = os.environ.get('BOT_TOKEN')
client = commands.Bot(command_prefix = '.')
connection_manager = database.ConnectionManager()

#answers with the ms latency
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

@client.command(pass_context=True)
async def send(ctx, args):
    await ctx.send({'user_id': ctx.message.author.id, 'args': str(args)})
    connection_manager.set_stats({'user_id': ctx.message.author.id, 'args': str(args)})
    await ctx.send('Updated database!')

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    print('test')



client.run(TOKEN)