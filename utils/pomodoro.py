import asyncio
from utils.pomodoro_utils import play_alarm, cancel, status

class Pomodoro:
    def __init__(self, ctx, pomodoro_duration=25, short_break_duration=5, long_break_duration=15):
        self.ctx = ctx
        self.pomodoro_duration = pomodoro_duration * 60 # convert minutes to seconds
        self.short_break_duration = short_break_duration * 60 # convert minutes to seconds
        self.long_break_duration = long_break_duration * 60 # convert minutes to seconds
        self.pomodoro_count = 0
        self.alarm = None
        self.current_task = None
        
    async def start(self):
        self.pomodoro_count += 1
        self.current_task = "pomodoro"
        await self.ctx.send(f"Pomodoro #{self.pomodoro_count} started for {self.pomodoro_duration//60} minutes!")
        self.alarm = asyncio.create_task(play_alarm(self.pomodoro_duration))
        await self.alarm
    
    async def short_break(self):
        self.current_task = "short_break"
        await self.ctx.send(f"Short break started for {self.short_break_duration//60} minutes!")
        self.alarm = asyncio.create_task(play_alarm(self.short_break_duration))
        await self.alarm
    
    async def long_break(self):
        self.current_task = "long_break"
        await self.ctx.send(f"Long break started for {self.long_break_duration//60} minutes!")
        self.alarm = asyncio.create_task(play_alarm(self.long_break_duration))
        await self.alarm
    
    async def play_alarm(self, duration):
        await play_alarm(duration)
        if self.current_task == "pomodoro":
            await self.short_break()
        elif self.pomodoro_count % 4 == 0:
            await self.long_break()
        else:
            await self.start()
    
    async def cancel(self):
        await cancel(self.ctx, self.alarm)
    
    async def status(self):
        await status(self.ctx, self.pomodoro_duration, self.short_break_duration, self.long_break_duration, self.pomodoro_count)
