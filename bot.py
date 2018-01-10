# Monika by Hal0
# A simple bot to RP and some mild reaction humor

import discord
import asyncio
import logging
import random


with open('token.txt') as token_file:
    TOKEN = token_file.read().strip()


client = discord.Client(game=discord.Game(name="The Piano"))

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
            await asyncio.sleep(0.2)
            await message.delete()
            tbs = tbs[7:]
            await message.channel.send(tbs)
        else:
            rand_spook = random.randint(1, 3)
            spooks = {1: "https://www.youtube.com/watch?v=w0RA_LZC0Jg", 2: "https://i.redd.it/w42owez9o6yz.png",
                      3: "https://vignette.wikia.nocookie.net/doki-doki-literature-club/images/2/2e/Act_3_Classroom.gif"
                      }
            await message.author.create_dm()
            dmchannel = message.author.dm_channel
            await dmchannel.send(spooks[rand_spook])

    if message.content.startswith('$8ball'):
        result = random.randint(1, 20)
        answers = {1: "It is certain", 2: "It is decidedly so", 3: "Without a doubt", 4: "Yes, definitely", 5:
                   "You may rely on it", 6: "As I see it, yes", 7: "Most likely", 8: "Outlook Good", 9: "Yes",
                   10: "Signs point to yes", 11: "Reply hazy try again", 12: "Ask again later",
                   13: "Better not tell you now", 14: "Cannot predict now", 15: "Concentrate and ask again",
                   16: "Don't count on it", 17: "My reply is no", 18: "My sources say no",
                   19: "Outlook not so good", 20: "Very Doubtful"}
        await message.channel.send(answers[result])

    # there are 47 lick gifs
    # ! important, update if changed
    if message.content.startswith('$lick'):
        lickresult = random.randint(1, 47)
        images = ["https://media.giphy.com/media/11o44A5ZoR4cZq/giphy.gif",
                  "https://media.giphy.com/media/kVDaetFZqnDXi/giphy.gif", "https://tenor.com/Mzb5.gif",
                  "https://tenor.com/ziBy.gif", "https://imgur.com/uyYwsr9", "https://imgur.com/Lc278Vq",
                  "https://imgur.com/CJOfHTX", "https://imgur.com/4epbp0E", "https://imgur.com/ZSswVM0",
                  "https://imgur.com/bnch1ir", "https://imgur.com/TLAOi7e", "https://imgur.com/J2Qx8ES",
                  "https://imgur.com/JVW0NsD", "https://imgur.com/CLV3C3b", "https://imgur.com/MiB5B9V",
                  "https://imgur.com/3HuTGtR", "https://imgur.com/Vgg2yT4", "https://imgur.com/MUXDYdo",
                  "https://imgur.com/CVOnurV", "https://imgur.com/sgBxTs6", "https://imgur.com/yRlgQCG",
                  "https://imgur.com/aYFAcHr", "https://imgur.com/fNZbK2K", "https://imgur.com/E7jQm5N",
                  "https://imgur.com/PzAtQkZ", "https://imgur.com/tqJ3vQM", "https://imgur.com/n1Z9rrd",
                  "https://imgur.com/Ud1NDGK", "https://imgur.com/uNz63bD", "https://imgur.com/5iGbpSR",
                  "https://imgur.com/ZuYMgpW", "https://imgur.com/bGq1pAu", "https://imgur.com/9dYNzzD",
                  "https://imgur.com/cyzm0Va", "https://imgur.com/qHDS9Ly", "https://imgur.com/gfR8NzL",
                  "https://imgur.com/85DT9Aj", "https://imgur.com/BfxOF4D", "https://imgur.com/XwCi9RR",
                  "https://imgur.com/U3m2j6o", "https://imgur.com/9V8YZyt", "https://imgur.com/drw9h4I",
                  "https://imgur.com/3rfKAQK", "https://imgur.com/M8ESfae", "https://imgur.com/bVy3PzS",
                  "https://imgur.com/tkQUdIM", "https://imgur.com/U8tzSCf"]
        await message.channel.send(images[lickresult])

    if message.content.startswith('$lenny'):
        await message.delete()
        await message.channel.send('( ͡° ͜ʖ ͡°)')

    if message.content.startswith('$scare'):
        await message.channel.send("https://i.redd.it/w42owez9o6yz.png")


client.run(TOKEN)
