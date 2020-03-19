import discord
from discord.ext import commands
import os
import requests, random, datetime, sys, time, argparse, os

client = discord.Client()
client = commands.Bot( command_prefix='>')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith('!info'):
        await message.channel.send(message.content)
       e = discord.Embed(title=message.author.name)
       await message.channel.send(message.content, embed=e)
    if message.content.startswith('!info'):
        id = await client.fetch_user(message.author.id)
        await message.channel.send(id) 
    print('Message from {0.author} : {0.content}'.format(message))'''
@client.event
async def on_member_join(member):
   ''' for channel in member.guild.channels:
        if str(channel) == "main": # We check to make sure we are sending the message in the general channel
            await channel.send(f"""Welcome to the server {member.mention}""")
    print(1)'''
   await member.create_dm()
   await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.command(pass_context = True)
async def voice(channel):
    print('>voice'+ str(channel))



#token = ''
#client.run(token)
token = os.environ.get('token')
client.run(str(token))
