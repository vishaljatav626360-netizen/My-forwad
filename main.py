import os
import asyncio
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# --- WEB SERVER CONFIG (For Render 24/7) ---
web = Flask(__name__)

@web.route('/')
def index():
    return "Bot is running perfectly!"

def run_flask():
    # Render default port 10000 use karta hai, par hum 8080 specify kar rahe hain
    web.run(host='0.0.0.0', port=8080)

# --- BOT CONFIG ---
# Naye Credentials jo tune diye
API_ID = 32920807
API_HASH = "43c7e7141a55e7ebece4e577fc808a7b"
# Session string Render ke Environment Variables se uthayega
SESSION = os.environ.get("SESSION_STRING")

SOURCE_ID = -1002050954054
TARGET_ID = -1003889448739

# Client Setup
app = Client(
    "my_forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

# --- FORWARDING LOGIC ---
@app.on_message(filters.chat(SOURCE_ID))
async def forward_msg(client, message):
    try:
        # copy() server-to-server kaam karta hai
        await message.copy(chat_id=TARGET_ID)
        print(f"✅ Message copied from {SOURCE_ID} to {TARGET_ID}")
    except Exception as e:
        print(f"❌ Error while forwarding: {str(e)}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Start Web Server
    print("🛰️ Starting Web Server...")
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    # 2. Start Bot
    print("🚀 Cloud Forwarder is starting...")
    try:
        app.run()
    except Exception as start_error:
        print(f"🔥 Critical Error: {str(start_error)}")
