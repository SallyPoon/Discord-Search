import logging
import requests

logging.basicConfig(level=logging.INFO)

import discord

client = discord.Client()

TOKEN = 'NTQ2MTIxMTgyMjk0ODM1MjEw.D0jmmg.EW2sBmhkW452XZe7jYhIT76SirQ';


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
    string = "\n".join("{}".format("["+text+"]("+url+')')for text, url
    in zip(results[1], results[links]))
    return string



@client.event
async def on_message(message):
    if message.content.startswith('$search'):
        words =  message.content.split(maxsplit = 1)
        words = words[1:]
        e = discord.Embed(title = words[0], description = searchWiki(words[0]))
        await client.send_message(message.channel, embed = e)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
