import discord
import asyncio

username = input("Username: ")
password = input("Password: ")


client = discord.Client()
@client.event
async def on_ready():
    print ("Logged in as: ")
    print ("Client Username: ", client.user.name)
    print ("Client ID: ", client.user.id)
    print("---------")

@client.event
async def on_message(message):
    if message.content.startswith('!calculatemessages'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=1500):
            if log.author == message.author:
                counter +=1
        await client.edit_message(tmp, "You have {} messages.".format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5) #Appears to be in seconds.
        await client.send_message(message.channel, 'Done sleeping.')

    elif message.content.startswith('!pythonhelp'):
       await client.send_message(message.channel, 'Need help with Python? Shoe recommends the Python Docs, Stack Exchange, and Google. (; ')

    elif message.content.startswith("!help"):
        await client.send_message(message.channel, "If you need help with something, tag (using the '@' symbol) Austin Archer or Jest.")

    elif message.content.startswith("!bothelp"):
        await client.send_message(message.channel, "If you need help with the bot, contact @Shoe. If the bot is spamming, contact @Austin Archer")

    elif message.content.startswith("!commands"):
        await client.send_message(message.channel, "Current commands can be found here: ")

    elif message.content.startswith("!GitHub"):
        await client.send_message(message.channel, "The GitHub repo for this project is here: https://github.com/Protonshoe/Aglets")
    elif message.content.startswith("!info"):
        await client.send_message(message.channel, "Bot version: 1.0.3")
        await client.send_message(message.channel, "Author: Shoe")
        await client.send_message(message.channel, "Currently in development. Use !GitHub for source.")


client.run(username, password)
<<<<<<< HEAD
input("Press a key to end....")
=======

>>>>>>> origin/master
