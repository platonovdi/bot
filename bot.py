import discord
from discord import VoiceChannel, channel, guild, member, message, role
client = discord.Client()


@client.event
async def on_ready():
    print('Logged on as {0} !'.format(client))
    


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith('!info'):
        await message.channel.send(message.content)
    if message.content.startswith('!info'):
        id = await client.fetch_user(message.author.id)
        await message.channel.send(id) 
    print('Message from {0.author} : {0.content}'.format(message))
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "main": # We check to make sure we are sending the message in the general channel
            await channel.send(f"""Welcome to the server {member.mention}""")
    print(1)

client.run('NTU1MTE3NTQ0NDUzODMyNzA0.XYPgvg.81VBwBzQPbx_lS4rERXKdoPL53Q')
