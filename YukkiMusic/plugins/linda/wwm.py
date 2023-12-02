from pyrogram import Client, filters
from datetime import datetime
from YukkiMusic import app


def get_current_time():
    tz = pytz.timezone('Asia/Riyadh')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@app.on_message(filters.command(["الوقت"],""))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"Current time in India: {time}")
