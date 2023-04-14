import asyncio

async def play_alarm(duration):
    await asyncio.sleep(duration)

async def cancel(ctx, alarm):
    if alarm:
        alarm.cancel()
        alarm = None
    await ctx.send("Pomodoro cancelled.")

async def status(ctx, pomodoro_duration, short_break_duration, long_break_duration, pomodoro_count):
    status_message = f"Current Pomodoro status:\n" \
                     f"Pomodoro duration: {pomodoro_duration//60} minutes\n" \
                     f"Short break duration: {short_break_duration//60} minutes\n" \
                     f"Long break duration: {long_break_duration//60} minutes\n" \
                     f"Pomodoro count: {pomodoro_count}"
    await ctx.send(status_message)
