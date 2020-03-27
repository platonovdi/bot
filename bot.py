import discord
from discord.ext import commands 
import qrcode
import os


client = discord.Client()
client = commands.Bot( command_prefix='->')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(status = discord.Status.idle, activity = discord.Game( 'Visual Studio Code' ))
    
@client.event
async def on_member_join(member : discord.Member):
    channel = client.get_channel( 555120639447662602 )
    role = discord.utils.get(member.guild.roles , id = 690290157999620116)
    await member.add_roles(role)
   
   
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def bot_status(ctx, *args):
    string = str()
    for i in args:
        string += str(i)
        string += ' '
    print(string)
    await client.change_presence(activity= discord.Game(f'{string}'))
    print(string + ' ')

@bot_status.error
async def status_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, у вас недостаточно прав! :clown:')


@client.command(pass_context = True)
async def qr(ctx , *args ):
    string = str()
    for i in args:
        string += str(i)
        string += ' '
    print(string)
    img = qrcode.make(string)
    img.save('qr.png')
    await ctx.send(file = discord.File( fp = 'qr.png'))


@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx , amount = 1000):
    await ctx.channel.purge(limit = amount)

@clear.error
async def clear_error(ctx , error):
    if isinstance(error , commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, у вас недостаточно прав! :clown:')
    
'''   
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def give_admin(ctx , member: discord.Member):
    await client.add_roles(ctx.author,roles = 624318900783284225)'''
#token = ''
#client.run(token)
token = os.environ.get('token')
client.run(str(token))
