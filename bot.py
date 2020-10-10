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
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    data.modify(AmongUsData.CREW_WIN,AmongUsData.INCREASE,1)
    connection_manager.update_stats_user('AmongUs',PlayerData(ctx.message.author.id), data)
    await ctx.send(f'Your crewmate win amount is now {data.crew_mate_wins}.')

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    print('test')

client.run(TOKEN)