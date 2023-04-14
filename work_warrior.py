from utils.pomodoro import Pomodoro

import discord
from discord.ext import commands, tasks
import asyncio
import time

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='start')
async def start_pomodoro(ctx, pomodoro_duration=25, short_break_duration=5, long_break_duration=15):
    pomodoro = Pomodoro(ctx, int(pomodoro_duration), int(short_break_duration), int(long_break_duration))
    await pomodoro.start()

@bot.command(name='cancel')
async def cancel_pomodoro(ctx):
    pomodoro = Pomodoro(ctx)
    await pomodoro.cancel()

@bot.command(name='status')
async def status_pomodoro(ctx):
    pomodoro = Pomodoro(ctx)
    await pomodoro.status()

bot.run('MTA5NjI5Mjc2MjUxNDY0MDk0Nw.GEPM12.i_l2EIShg5ubtK2IaCvIpiarzCgDNBGFw6iiPw')
