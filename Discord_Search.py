import logging
import requests

logging.basicConfig(level=logging.INFO)

import discord


TOKEN = 'NTQ2MTIxMTgyMjk0ODM1MjEw.D0jmmg.EW2sBmhkW452XZe7jYhIT76SirQ'

client = discord.Client()

@client.event
async def on_message(message):
    def __repr__(self):
        return str(self.__dict__)
    if message.content.startswith('$search'):
        search =  message.content.split(maxsplit = 1)
        search = search[1:];
        response = requests.get('//wiki.mabinogiworld.com/api.php')
        print(response.status_code);
        #await client.send_message(message.channel, search)
        # message = await client.wait_for_message(author=message.author, check=check)
        # name = message.content[len('$name'):].strip()
        # await client.send_message(message.channel, '{} is stinky'.format(name))



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
