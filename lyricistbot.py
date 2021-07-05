import discord
import lyricsgenius as genius
from lyricsgenius.api.public_methods import song
import config


api = genius.Genius('')
api = genius.Genius(config.GENIUS_TOKEN)

from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = ''
TOKEN = config.BOT_TOKEN

client = commands.Bot(command_prefix = '$')
client.remove_command("help")
@client.event
async def on_ready():
  print('Bot is ready!')

@client.command(aliases=['hi','hello','Hello'])
async def Hi(ctx):
    await ctx.channel.send("What's up!")


@client.command()
async def sng(ctx,*arg):
  string=''
  s=''
  string = arg
  for str in string:
    s = s + " "+ str

  s
  lyrics_list=[]
  await ctx.channel.send("Searching for lyrics to {}..,".format(s))
  song = api.search_song(s)
  if song:
      url = song.url
      await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(url))
      lyrics = song.lyrics.split("\n")
      for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            #lyrics_str+=line
            lyrics_list.append(line)
            #await ctx.channel.send("{}".format(line))
      #await ctx.channel.send(lyrics_str) #sending the lyrics in one ugly string

  embed= discord.Embed(
        title = 'Embedded lyrics',
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.random() 
    )
  
  await ctx.channel.send(embed=embed) #ctx.send

@client.command()
async def lyr(ctx, *arg):
  string = ''
  a=''
  s=''
  string = arg
  for str in string:
    if(str == '~'):
      break
    a = a + " " + str

  a
  lyrics_str=''
  lyrics_list=[]
  s_ = string[string.index('~') : len(string)]
  for _s in s_ :
    if(_s == '~'):
      continue
    s = s + " " + _s

  s
  await ctx.channel.send("Searching for the lyrics to {} by {} ...".format(s, a))
  song = api.search_song(s, a)
  if song:
      url = song.url
      await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(url))
      lyrics = song.lyrics.split("\n")
      for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            #lyrics_str+=line
            lyrics_list.append(line)
            #await ctx.channel.send("{}".format(line))
      #await ctx.channel.send(lyrics_str) #sending the lyrics in one ugly string

  embed= discord.Embed(
        title = 'Embedded lyrics',
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.random() 
    )
  
  await ctx.channel.send(embed=embed) #ctx.send

  

#for help
@client.command()
async def help(ctx):
    embed= discord.Embed(
        title = 'Lyricist command list',
        description = 'Here you can find a list of commands you can use.',
        colour = discord.Colour.random() 
    )
    embed.add_field(name='$help',value='Use this command to get help about how to use the bot.',inline = True)
    embed.add_field(name='$lyr',value='Use this command to get lyrics of songs.(used as $lyr song_name)',inline = True)
    
    embed.set_thumbnail(url='https://picsum.photos/200/300')

    await ctx.channel.send(embed=embed)

client.run(TOKEN)
