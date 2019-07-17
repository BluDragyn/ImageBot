import discord
from discord.ext import commands
import asyncio
import random
import os
import string
import sys
import aiohttp
from urlextract import URLExtract
import aiofiles
from config import *
from time import sleep
import logging
import time

# BEGIN BOT CONFIGURATION

bot = commands.Bot(description='Custom Image bot for www.TheKinkyPlace.net', command_prefix = '!')
date = time.strftime('%Y%m%d')
logging.basicConfig(level = logging.INFO, filename = date + '.log', filemode = 'a+', format='%(asctime)-15s %(levelname)-8s %(message)s')

# END BOT CONFIGURATION

def getChannelID(cat):
  if cat == 'anal': #First category
    id = anal
  elif cat == 'ass': #Second Category
    id = ass
#Repeat for each category
  return id

@bot.event
async def on_ready():
  print('Logged in as')
  print('Username: ' + bot.user.name)
  print('Client ID: ' + str(bot.user.id))
  print('--------------')
  print('ImageBot READY!')
  logging.info('Logged in.')

@bot.event
async def on_message(message):
  #Deletes all non-image posts on "selfie" channel
  if message.channel.id == submissions and not message.attachments and not message.embeds:
    await message.delete()
  if message.content.lower().startswith(prefix):
    cat = message.content.strip(prefix)
    if cat in categories:
      id = getChannelID(cat)
      imgList = os.listdir(library + cat + '/')
      imgString = random.choice(imgList)
      path = library + cat + '/' + imgString
      channel = bot.get_channel(id)
      await channel.send(file=discord.File(path))
      logging.info('-> ' + str(message.author) + ' used command: ' + cat.upper())
      print('-> ' + str(message.author) + ' used command: ' + cat.upper())
      sleep(5)


bot.run(token)
