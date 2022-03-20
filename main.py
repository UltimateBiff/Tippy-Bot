#the import from the "Secrets(Environment variables)"
import os

#imports by discord that make the give you the ability to program commands into the bot
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

#imports replit's data base
from replit import db

#this import allows you to have the program choose something random for you
import random

#This is variable that is very important to make the commands work
client = discord.Client()

#to give the bot a prefix and make it not case sensitive
client = commands.Bot(command_prefix = '', case_insensitive=True) #NOTE: if you want the bot to be case sensitive then just don't put that part of the code in

#to get the console to tell you when the bot is ready to use
@client.event
async def on_ready():
	print('ok your good to go')

# If You Say Tippy He Meows
@client.command()
async def Tippy(ctx):
	await ctx.send("Meow")

# If You Say Ping He Pongs
@client.command()
async def Ping(ctx):
	await ctx.send("Pong")

# If You Say Pong He Pings
@client.command()
async def Pong(ctx):
	await ctx.send("Ping")

# If You Say Meow He Will Give A Random Response
response = ["Feed Me", "Mow", "Give Snacks"]
@client.command()
async def Meow(ctx):
	await ctx.send(random.choice(response))

# Will Repeat A Word
@client.command()
async def TippySay(ctx, arg):
	await ctx.send(arg)

#a command that picks a random word out of the words you tell it
@client.command()
async def TippyDecide(ctx, *arg):
	await ctx.send("I choose: " + random.choice(arg)) #as you can see I have so that it will start with "I choose " then it will pick one of the words you said at random and add that to it

#a command where the bot will say "your name is bland and you are blank years old."
@client.command()
async def TyeInsult(ctx, arg1, arg2):
	await ctx.send("Tye is " + arg1 + " and smells like " + arg2 + " LMAO.")

#sPlugs His Youtube
@client.command()
async def TippyOfficial(ctx):
	easy_embed=discord.Embed(title="Subscribe To Tippy", url="https://www.youtube.com/channel/UCy3N-C4EIxIzYeilWWYbf7A", description="Subscribe", color=0x051878)
	await ctx.send(embed=easy_embed)


#embed with an author (unused)
@client.command()
async def embedtwo(ctx):
	author_embed=discord.Embed(title="This is an embed", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", description="This is a discription", color=0x051878)
	author_embed.set_author(name="Author's name", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", icon_url="https://cdn.discordapp.com/attachments/833008810029088829/838230626628534272/compass_of_east.jpeg") # if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)# if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)
	await ctx.send(embed=author_embed)

#embed with a footer (unused)
@client.command()
async def embedthree(ctx):
	footer_embed=discord.Embed(title="This is an embed", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", description="This is a discription", color=0x051878)
	footer_embed.set_author(name="Author's name", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", icon_url="https://cdn.discordapp.com/attachments/833008810029088829/838230626628534272/compass_of_east.jpeg") # if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)# if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)
	footer_embed.set_footer(text="footer") # and you can add a "icon_url" just like in the author
	await ctx.send(embed=footer_embed)

#embed with thumbnail (unused)
@client.command()
async def embedfour(ctx):
	thumbnail_embed=discord.Embed(title="This is an embed", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", description="This is a discription", color=0x051878)
	thumbnail_embed.set_author(name="Author's name", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", icon_url="https://cdn.discordapp.com/attachments/833008810029088829/838230626628534272/compass_of_east.jpeg") # if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)# if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)
	thumbnail_embed.set_footer(text="footer") # and you can add a "icon_url" just like in the author
	thumbnail_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/833008810029088829/838559415346266123/phx.png")
	await ctx.send(embed=thumbnail_embed)

@client.command()
async def embedfive(ctx):
	extrafield_embed=discord.Embed(title="This is an embed", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", description="This is a discription", color=0x051878)
	extrafield_embed.set_author(name="Author's name", url="https://learn-to-program-a-bot-web.cuber1515.repl.co/", icon_url="https://cdn.discordapp.com/attachments/833008810029088829/838230626628534272/compass_of_east.jpeg") # if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)# if you want to make the name be the name of who ever used the command then just put "ctx.author.display_name"(without the quotes around it) and for the picture to be the users pfp just put "ctx.author.avatar_url" (without the quotes around it)
	extrafield_embed.set_footer(text="footer") # and you can add a "icon_url" just like in the author
	extrafield_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/833008810029088829/838559415346266123/phx.png")
	extrafield_embed.add_field(name="Field Number 1", value="This is not inline and as you can see it takes up the whole section", inline=False)
	extrafield_embed.add_field(name="Field Number 2", value="This is inline and shares a space with the next field", inline=True)
	extrafield_embed.add_field(name="Field Number 3", value="This is inline and shares a space with the next field", inline=True)
	await ctx.send(embed=extrafield_embed)

#Uhhhh
@client.command()
async def Cat(ctx):
	await ctx.send("Meow \nMow")
	


#to connect the this page of code to the bot if you want to connect your bot to this you must conncet the bot's token with a `Environment variable`. make the `key` "TOKEN", and put the bot's token in `value`
#NOTE: keep this line of code underneath everything else
client.run(os.getenv('TOKEN'))