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
async def crewwin(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    data.modify(AmongUsData.CREW_WIN,AmongUsData.increase,1)
    connection_manager.update_stats_user('AmongUs',PlayerData(ctx.message.author.id), data)
    await ctx.send(f'Your crewmate win amount is now {data.crew_mate_wins}.')

@client.command(pass_context=True)
async def crewloss(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    data.modify(AmongUsData.CREW_LOSS,AmongUsData.increase,1)
    connection_manager.update_stats_user('AmongUs',PlayerData(ctx.message.author.id), data)
    await ctx.send(f'Your crewmate loss amount is now {data.crew_mate_losses}.')

@client.command(pass_context=True)
async def impostorwin(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    data.modify(AmongUsData.IMPOSTOR_WIN,AmongUsData.increase,1)
    connection_manager.update_stats_user('AmongUs',PlayerData(ctx.message.author.id), data)
    await ctx.send(f'Your impostor win amount is now {data.impostor_wins}.')

@client.command(pass_context=True)
async def impostorloss(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    data.modify(AmongUsData.IMPOSTOR_LOSS,AmongUsData.increase,1)
    connection_manager.update_stats_user('AmongUs',PlayerData(ctx.message.author.id), data)
    await ctx.send(f'Your impostor loss amount is now {data.crew_mate_losses}.')

@client.command(pass_context=True)
async def getcrewwin(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    await ctx.send(f'Your crewmate win amount is {data.crew_mate_wins}.')

@client.command(pass_context=True)
async def getcrewloss(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    await ctx.send(f'Your crewmate loss amount is {data.crew_mate_losses}.')

@client.command(pass_context=True)
async def getimpostorwin(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    await ctx.send(f'Your impostor win amount is {data.impostor_wins}.')

@client.command(pass_context=True)
async def getimpostorloss(ctx, *args):
    data = AmongUsData.from_dict(connection_manager.get_data('AmongUs', PlayerData(ctx.message.author.id)),ctx.message.author.id)
    await ctx.send(f'Your impostor loss amount is {data.crew_mate_losses}.')

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')
    print('test')

client.run(TOKEN)