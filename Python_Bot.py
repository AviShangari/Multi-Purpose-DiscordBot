import discord
import os
import subprocess
import json
import webbrowser
import AutomatedSchedule
from discord.ext import commands
import YoutubeMusicPlayer
import AudioManager


bot = commands.Bot(command_prefix="-")


def get_token():

    token = []
    f = open('DiscordToken.txt')

    for line in f:
        token.append(line)

    f.close()
    return token[0]


@bot.command()
async def active(ctx):
    await ctx.send("```Hey, I am right here!```")


@bot.command()
async def send(ctx, name: str):
    temp = ''
    for root, dirs, files in os.walk(r"C:\\Users\\COCRe\\Downloads"):
        if name in files:
            temp = os.path.join(root, name)
    await ctx.send(file=discord.File(temp))


@bot.command()
async def run(ctx, name):
    with open("discord_app_paths.json") as json_file:
        data = json.load(json_file)
    subprocess.call(data[name])
    await ctx.send("```Opening " + name + "...```")


@bot.command()
async def study(ctx):
    webbrowser.open("https://learn.ontariotechu.ca/")
    await ctx.send("```Opening study tabs...```")


@bot.command()
async def watch(ctx, name):
    if name == "netflix":
        webbrowser.open("```https://www.netflix.com/browse```")
        await ctx.send("Opening Netflix...")
    elif name == "youtube":
        webbrowser.open("www.youtube.com")
        await ctx.send("```Opening Youtube...```")
    else:
        await ctx.send("```Invalid Selection!```")


@bot.command()
async def schedule(ctx):
    await ctx.send('```Getting the schedule...```')
    await ctx.send(AutomatedSchedule.schedule_to_string())


@bot.command()
async def play(ctx, *args):
    song = ""
    for word in args:
        song += word + " "
    await ctx.send('```Playing: ' + song + "```")
    YoutubeMusicPlayer.play_song(song)


@bot.command()
async def pause(ctx):
    YoutubeMusicPlayer.pause()
    await ctx.send('```Song Paused```')


@bot.command()
async def resume(ctx):
    YoutubeMusicPlayer.play()
    await ctx.send('```Song Resumed```')


@bot.command()
async def repeat(ctx, word: str):
    if word.lower() == 'song':
        YoutubeMusicPlayer.repeat('song')
        await ctx.send('```Repeating current song```')
    elif word.lower() == 'off':
        YoutubeMusicPlayer.repeat('off')
        await ctx.send('```Repeat for this song has been turned off```')
    else:
        await ctx.send('```You have entered an incorrect command. Please try again.```')


@bot.command()
async def volume(ctx, vol: float):
    await ctx.send("```Setting volume to: " + str(vol) + "```")
    AudioManager.set_volume(vol)

YoutubeMusicPlayer.log_in()
AutomatedSchedule.log_in()
bot.run(get_token())
