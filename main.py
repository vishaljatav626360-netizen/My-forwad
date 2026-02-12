from pyrogram import Client, filters
import os

# Credentials
API_ID = 21975825 
API_HASH = "85223c21c60a9202167d6092d6e38b36"
# Render par hum SESSION_STRING use karenge taaki login baar-baar na karna pade
SESSION = os.environ.get("SESSION_STRING") 

SOURCE = -1002050954054
TARGET = -1003889448739

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@app.on_message(filters.chat(SOURCE))
async def forward(client, message):
    try:
        await message.copy(chat_id=TARGET)
    except Exception as e:
        print(f"Error: {e}")

print("🚀 Cloud Forwarder is Running...")
app.run()
