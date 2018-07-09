import discord

from matchmaking import Matcher

TOKEN = 'NDY1OTAwODU4MTY5NjIyNTI5.DiUPlg.SuNGGmXc4aaY3j5DjrCDUaGH8rg'

client = discord.Client()
matcher = Matcher()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!vamos'):
        msg = 'Vamos Lá! https://www.youtube.com/watch?v=nBUgK680nVg&t=14s'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!m'):
        queue = matcher.check_queue_for_players()
        msg = 'Hep'
        await client.send_message(message.channel, msg)
        if queue is not None:
            msg = ('Players in queue: ' + str(queue)).format(message)
        else:
            msg = 'Currently no players in the queue. Adding {0.author.mention} in queue'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
