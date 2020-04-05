import discord
from discord.ext import commands 
import qrcode
import os
import json
from func import level_up, add_experience,update_data


client = discord.Client()
client = commands.Bot( command_prefix='->')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    custom_activity = discord.Streaming(name = 'Bot',url = 'https://github.com/platonovdi/bot')
    await client.change_presence(status = discord.Status.idle, activity = custom_activity)



@client.event
async def on_member_join(member : discord.Member):
    channel = client.get_channel( 555120639447662602 )
    role = discord.utils.get(member.guild.roles , id = 690290157999620116)
    await member.add_roles(role)
   


    with open('users.json', 'r') as f:
        users = json.load(f)
 
 
    await update_data(users, member)
 
   
    with open('money.json', 'w') as f:
        json.dump(users, f)
   

    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
      await ctx.send(embed = discord.Embed(description = f':exclamation:{ctx.author.mention},Данной команды   не существует. :clown:', color=0xff0000)) 

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
        await ctx.send(embed = discord.Embed(description = f':exclamation:{ctx.author.mention}, у вас недостаточно прав! :clown:', color=0xff0000))

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
        await ctx.send(embed = discord.Embed(description = f':exclamation:{ctx.author.mention}, у вас недостаточно прав! :clown:',color = 0xff0000))
    
@client.command(pass_context = True)
async def lvl(ctx):
    author = ctx.author
    await ctx.send(author.id)
'''   
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def give_admin(ctx , member: discord.Member):
    await client.add_roles(ctx.author,roles = 624318900783284225)'''

#token = ''
#client.run(token)
    
@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
 
 
        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)
   
   
        with open('users.json', 'w') as f:
            json.dump(users, f)
 

token = os.environ.get('token')
client.run(str(token))