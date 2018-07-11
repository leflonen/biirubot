import discord
import logging

from matchmaking import Matcher

TOKEN = ''

client = discord.Client()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('biirubot')

@client.event
async def on_message(message):
    matcher = Matcher(logger)
    if message.author == client.user:
        return

    if message.content.startswith('!vamos'):
        logger.info('Sending Vamos')
        msg = 'Vamos Lá! https://www.youtube.com/watch?v=nBUgK680nVg&t=14s'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!m'):
        logger.info('Matchmaking')
        queue = matcher.check_queue_for_players()
        logger.info(queue)
        if queue is not None:
            msg = ('Players in queue: ' + str(queue)).format(message)
        else:
            msg = 'Currently no players in the queue. Adding {0.author.mention} in queue'.format(message)
            if len(message.content.split()) == 1:
                matcher.add_player_to_queue('{0.author.mention}'.format(message), 'any')
            elif len(message.content.split()) == 2:
                matcher.add_player_to_queue('{0.author.mention}'.format(message), message.content.split()[1])
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
