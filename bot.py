from os import name
import discord
import praw
import random

reddit = praw.Reddit(client_id = "<CLIENT ID>",
client_secret = "<CLIENT SECRET>",
username = "<USERNAME>",
password = "<PASSWORDS>",
user_agent = "<THE USER ID")

from discord.ext import commands
imlist=["im","i'm", "i am"]
client=commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    print("ooga booga bot ooga booga")
@client.command()
async def meme(ctx,subreds = "SaimanSays"):
    subreddit = reddit.subreddit(subreds)
    all_subs = []
    top = subreddit.top(limit = 50)
    for memes in top:
        all_subs.append(memes)
    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    embedss = discord.Embed(title = name)
    embedss.set_image(url = url)

    await ctx.send(embed = embedss)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'hi':
        await message.channel.send('Hi there')
    for i in imlist:
        if message.content.lower().startswith(i):
            mainmessage="Hi "+message.content.replace(i,"",1)+" i'm dad"

            await message.channel.send(mainmessage)
    await client.process_commands(message)
client.run("<BOT TOKEN>")

