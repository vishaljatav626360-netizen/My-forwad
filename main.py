from pyrogram import Client, filters
import os

# Naye Credentials
API_ID = 32920807
API_HASH = "43c7e7141a55e7ebece4e577fc808a7b"
SESSION = os.environ.get("SESSION_STRING") 

SOURCE = -1002050954054
TARGET = -1003889448739

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@app.on_message(filters.chat(SOURCE))
async def forward(client, message):
    try:
        # Copying without downloading (0% storage)
        await message.copy(chat_id=TARGET)
    except Exception as e:
        print(f"Error: {e}")

print("🚀 Cloud Forwarder is Running...")
app.run()
