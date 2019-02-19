import logging
import requests

logging.basicConfig(level=logging.INFO)

import discord


TOKEN = 'NTQ2MTIxMTgyMjk0ODM1MjEw.D0jmmg.EW2sBmhkW452XZe7jYhIT76SirQ'

client = discord.Client()

url = 'http://wiki.mabinogiworld.com/api.php'
def searchWiki(query):
    links = 3
    response = requests.get(url, params = {"action": "opensearch",
    		"format": "json",
    		"formatversion": 2,
    		"search": query,
    		"namespace": 0,
    		"limit": 5,
    		"suggest": True,})
    results = response.json()
    string = "\n".join("{} {}".format(text, url) for text, url in zip(results[1], results[links]))
        # string = "\n".join("{} {}".format(b))
        # string = "\n".join("{} {}".format(c))
        # string = "\n".join("{} {}".format(d))
        # string = "\n".join("{} {}".format(e))
    return string
            # http://wiki.mabinogiworld.com/api.php?action=opensearch&
            # format=json&search=query&namespace=0&limit=10&suggest=True)



@client.event
async def on_message(message):
    if message.content.startswith('$search'):
        words =  message.content.split(maxsplit = 1)
        words = words[1:]
        await client.send_message(message.channel, searchWiki(words[0]))
        #await client.send_message(message.channel, results)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
