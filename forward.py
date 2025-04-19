import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv
import os


# ---------------- CONFIGURATION ----------------
load_dotenv("apiprivate.env")
api_id = int(os.getenv('api_id'))
api_hash = os.getenv('api_hash')
session_name = 'forwarder_bot'
target_group_id = int(os.getenv('target_group_id'))

# ---------------- CLIENT SETUP ----------------
client = TelegramClient(session_name, api_id, api_hash)


# ---------------- HANDLERS ----------------
@client.on(events.NewMessage(incoming=True))
async def forward_private_messages(event):
    if event.is_private:  # Only handle private chats
        try:
            await client.forward_messages(
                entity=target_group_id,   # Where to forward
                messages=event.message.id,  # Message ID to forward
                from_peer=event.chat_id    # Where it came from
            )
            print(f"Forwarded a message from {event.chat_id} to group.")
        except Exception as e:
            print(f"Failed to forward message: {e}")


# ---------------- MAIN ----------------
async def main():
    print("Bot is running and listening for private messages...")
    await client.start()
    await client.get_dialogs()
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
