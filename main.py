#import statements
import os
import discord
from discord.ext import commands
from replit import db

#initialisation
intents=discord.Intents.default()
intents.members=True
client=commands.Bot(intents=intents,command_prefix='!')
guild_id= #initialise with guild_id
channel_id= #initialise with channel id
role_id= #initialise with roll_id
TOKE= #initialise with BotAuth TOKEN

#helper functions
#add names to the database
def add(name):
  if 'name' in db.keys():
    values=db['name']
    print(values)
    if name in values:
      return -1
    else:
      values.append(name)
      db['name']=values
      return 1
  else:
    db['name']=[name]
    return 1

#retrieve names from the database
def retNames():
  try:
    names=db['name']
    return names
  except:
    return "User Database not created"

#initialising bot
@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

#event reference: greeting message
@client.event
async def on_member_join(member):
  guild=client.get_guild(guild_id)
  channel=guild.get_channel(channel_id)
  await channel.send(f"Welcome {member.mention} ! :partying_face:")

#event reference: reaction acknowledgement
@client.event
async def on_reaction_add(reaction,user):
  channel=reaction.message.channel
  await channel.send(f"{user.display_name} reacted to {reaction.message.author.display_name}")

#command for creating new role
@client.command()
async def new_role(ctx,role_name):
  guild=ctx.guild
  memb=ctx.author
  role=await guild.create_role(name=role_name)
  await memb.add_roles(role)

#command for registering name
@client.command()
async def register(ctx,name):
  x=add(name)
  if(x==-1):
    await ctx.channel.send("Error: Name already registered ")
  else:
    await ctx.channel.send("Registered succesfully")

#command for retrieving name from database
@client.command()
async def retrieve_name(ctx):
  member=ctx.author
  r=ctx.guild.get_role(role_id)
  if r in member.roles:
    ls=''
    name_List=retNames()
    for i in name_List.value:
      ls=ls+i+'\n'
    await ctx.channel.send(ls)
  else:
    await ctx.channel.send("You are not authorised to perform this operation")

#makeing connection with bot user
client.run(TOKEN)
