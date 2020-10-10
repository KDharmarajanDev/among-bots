import os
import database
import discord
from player_data import PlayerData
from among_us_data import AmongUsData
from discord.ext import commands

TOKEN = os.environ.get('BOT_TOKEN')
client = commands.Bot(command_prefix = '.')
connection_manager = database.ConnectionManager()

#answers with the ms latency
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')

@client.command(pass_context=True)
async def win(ctx, *args):
    data = connection_manager.get_data('AmongUs',PlayerData(ctx.message.author.id))
    if data != None:
        data['crew_mate_wins'] += 1
    else:
        data = AmongUsData(ctx.message.author.id, 1).toDict()
    connection_manager.update_stats_user('AmongUs',PlayerData(ctx.message.author.id), data)
    await ctx.send(f'Your win amount is now {data["crew_mate_wins"]}')

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    print('test')

client.run(TOKEN)