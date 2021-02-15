import discord
from discord.ext import commands
import os
import praw
import random
# discord client object

client = commands.Bot(command_prefix='.')

CHANNEL_ID = '#YOUR CHANNEL ID'
# Do Stuff

#this bot uses reddit api to extract memes from the internet
#so we need to create one before we get started


reddit = praw.Reddit(client_id='#CLIENT ID',
                     client_secret='#CLIENT SECRET KEY',
                     user_agent='Dank Memer')



@client.command(name='memes')
async def version(context):
    memes_submissions = reddit.subreddit('memes').new()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await context.message.channel.send(submission.url)

@client.command(name='dankmemes')
async def version(context):
    memes_submissions = reddit.subreddit('dankmemes').new()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await context.message.channel.send(submission.url)

@client.command()
async def ping(context):
    await context.message.channel.send(f'{round(client.latency * 1000)} ms')

@client.command(aliases=['dark memer','imagine'])
async def darkmemer(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."
                 "I would rather not say that",
                 "I would rather go and hang myself than reply to this question",
                 "Can u guys stop, I am tired!!!",
                 "Most probably ",
                 "Trust me, yessss!!",
                 "another question ",
                 "LOL, yes!",
                 "DND",
                 "How to answer that??",
                 "yupp",
                 "cannot say",
                 "Obviously",
                 "Definitely not",
                 "Totally",
                 "That’s not true",
                 "Shut Up",
                 "Whatever",
                 "Never",
                 "That's wrong",
                 "True story"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

 #you can add more replies to the questions to people but bascially they should be yes or no


#google feature
@client.command(name='google')
async def google(ctx, *, question):
    count = 0
    try:
        from googlesearch import search
    except ImportError:
        pass
    for i in search(query=question, tld='co.in', lang='en', num=10, stop=1, pause=2):
        count += 1
        await ctx.message.channel.send(i)


#wikipedia search feature

@client.command(name='wiki')
async def google(ctx, *, question):
    count = 0
    try:
        from googlesearch import search
    except ImportError:
        pass

    for i in search(query=question + " wikipedia ", tld='co.in', lang='en', num=10, stop=1, pause=2):
        count += 1
        await ctx.message.channel.send(i)





#real bot command

@client.command(name='version')
async def version(context):
    Embeded_text = discord.Embed(title="Dark Memer", color=0x00ff00)
    Embeded_text.add_field(name="Version Code", value="v1.0.0", inline=False)
    Embeded_text.add_field(name="Date Released", value="not yet released ;)", inline=False)
    Embeded_text.set_footer(text="Version 2 coming soon")
    Embeded_text.set_author(name="Harshit")

    await context.message.channel.send(embed=Embeded_text)


#client events

@client.event
async def on_ready():
    general_channel = client.get_channel(CHANNEL_ID)
    await general_channel.send('Bot Started')



@client.event
async def on_message(message):

    if message.content == 'who are you':
        general_channel = client.get_channel(CHANNEL_ID)
        await general_channel.send('I a discord bot !!!')

    await client.process_commands(message)


# Run the client on the server

client.run('#DISCORD PRIVATE KEY ')
