import discord
from discord.ext import commands        #important to have discord.py downloaded

intents = discord.Intents.all()     #make whatever Intents you want

client = commands.Bot(command_prefix="!", intents=intents)      #our command is triggerted by !

@client.event       #when code is ready it will send message into console
async def on_ready():
    print("im ready :)")    #insert your text
    print("--------------")     #not important only for a good look

#your command into 
@client.command()
async def text(ctx): #TEXT = on what message it will react == !text
    await ctx.send("your text") #after !text will send message into the same channel as !text was send

@client.command()
async def tag(ctx, user: discord.Member):   #after !tag @user 
    await ctx.message.delete()  #delete !tag @user
    await ctx.send(f"your text <@{user.id}> your text") #message == "your text @user your text"

#new member join
@client.event
async def on_member_join(member):   #event on member join
    channel = member.guild.system_channel   #same channel as original (discord) welcome message was send
    if channel is not None:
        welcome_message = f">>> {member.mention} \n **Welcome to the server!**"     #insert your text
        await channel.send(welcome_message)     #send message on_member_join
    


client.run('Your server Code') #your original BOT code
