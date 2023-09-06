import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

music_queue = []

# Checking for songs in queue
def queue_check(ctx):
  if len(music_queue) > 0:
    voice_channel = ctx.voice_client
    source = music_queue.pop(0)
    voice_channel.play(source)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
# END OF UTILITY CODE

client = commands.Bot(command_prefix="a$")

# COMMANDS START HERE --------------------------------------------->
# JOIN COMMAND
@client.command(name="join", help="Connects Friday to a VoiceChat")
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
  else:
    await ctx.send("You're not in a Voice Channel")

# DISCONNECT COMMAND
@client.command(name="disconnect", help="Disconnects Friday from VoiceChat")
async def disconnect(ctx):
  try:
    await ctx.voice_client.disconnect()
    await ctx.send("Voice Chat Deactivated!")
  except:
    await ctx.send("Voice Chat not connected!")

#PLAY COMMAND
@client.command(name='play', help='Plays a song or soundtrack.')
async def play(ctx, url):
    # Checking for Voice Connectivity
    if not ctx.message.author.voice:
        await ctx.send("You're not connected to a voice channel!")
        return
    else:
        channel = ctx.message.author.voice.channel
        # Checking if the bot is in a voice channel
        if ctx.voice_client is None:
          await channel.connect()
  
    server = ctx.message.guild
    voice_channel = server.voice_client
    
    # If the queue is not empty, play from the queue
    async with ctx.typing():
      player = await YTDLSource.from_url(url, loop=client.loop)
      voice_channel.play(player, after=lambda e: queue_check(ctx))

      await ctx.send('**Now playing:** {}'.format(player.title))
        
# PAUSE COMMAND
@client.command(name="pause", help="Pauses a song or soundtrack.")
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  # Checking for Audio Playback
  if voice.is_playing():
    voice.pause()
    await ctx.send("Queue Paused!")
  else:
    return

# RESUME COMMAND
@client.command(name="resume", help="Resumes any paused music or soundtrack.")
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  voice.resume()
  await ctx.send("Resuming Queue..")

# QUEUE Command
@client.command(name="queue", help="Adds song to current music queue.")
async def queue(ctx, url):
  if not ctx.message.author.voice:
    await ctx.send("You're not in a Voice Channel!")
  else:
    # If the author is connected to a Voice channel 
    voice = ctx.voice_client
    # If a song is currently being played
    if voice.is_playing():
      player = await YTDLSource.from_url(url, loop=client.loop)
      music_queue.append(player)
      await ctx.send("Song added to Queue..")
    else:
      ctx.send("Nothing but, Cricket Noise...")

# DISPLAY COMMAND
@client.command(name="display", help="Displays the contents of the music queue.")
async def display(ctx):
  if len(music_queue) > 0:
    for track in music_queue:
      await ctx.send(track.title)
  else:
    await ctx.send("Cricket Noise indicates Queue is empty..")

# STOP COMMAND  
@client.command(name="stop", help="Stops all bot actions.")
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
  voice.stop()
  await ctx.send("Music Stopped.")

# Friday ACTIVATE COMMAND
@client.command(name="friday", help="Command to check if Friday is ready for action!")
async def friday(ctx):
  await ctx.send("Friday, at your service!") 

client.run("token")
