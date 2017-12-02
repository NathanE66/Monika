# Monika by Hal0
# A simple bot to RP and some mild reaction humor

import discord
import logging

with open('token.txt') as token_file:
    TOKEN = token_file.read().strip()


client = discord.Client()

logging.basicConfig(level=logging.INFO)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Monika'):
        if message.author.id == 113381929637662720:
            tbs = message.content
            await message.delete()
            tbs = tbs[7:]
            await message.channel.send(tbs)


client.run(TOKEN)
