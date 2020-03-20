import discord
from discord.ext import commands
import os


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
    channel = client.get_channel( 555120639447662602 )
    role = discord.utils.get(member.guild.roles , id = 690290157999620116)
    await member.add_roles(role)
   
   
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.command(pass_context = True)
async def voice(channel):
    print('>voice'+ str(channel))


@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx , amount = 1000):
    await ctx.channel.purge(limit = amount)
@clear.error
async def clear_error(error, ctx):
    if isinstance(error):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)
#token = ''
#client.run(token)
token = os.environ.get('token')
client.run(str(token))
