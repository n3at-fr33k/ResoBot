import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

#This line defines the client variable which will be used a lot in coding commands.
client = Bot(description = "ResoBot made by On!on#5333", command_prefix = "reso ")

@client.event
async def on_ready():
    #This function sets the Playing status for the bot
    await client.change_presence(activity = discord.Game("in development v1.0.0 alpha"))
    #The following lines print some information about the bot to the console
    print("=" * 40 + "\n")
    print("Logged in as: {}".format(client.user.name))
    print("Bot's clientID: {}\n".format(client.user.id))
    print("Connected to {} guilds".format(len(client.guilds)))
    print("Connected to {} users\n".format(sum(1 for user in client.get_all_members())))
    print("Running discord.py version {}".format(discord.__version__))
    print("Running Python version {}\n".format(platform.python_version()))
    print("Invite your bot: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8\n".format(client.user.id))
    print("="  * 40)

#Basic ping command - if you type ping with your prefix, it'll respond
@client.command()
async def ping(ctx):
    await ctx.send(":ping_pong: **Pong!**")

@client.command(brief='See what guild you are in.')
async def guild(ctx):
    await ctx.send(ctx.guild)

@client.command(brief='Use quotes for your message.')
async def echo(ctx, arg):
    await ctx.send(arg)

#Every bot has a unique token - insert your bot's token within the quotation marks
client.run("NoStealingMyTokenSmurf;/")
