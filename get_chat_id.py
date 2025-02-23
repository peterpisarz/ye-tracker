# get_chat_id.py
import asyncio
from telegram import Bot

TOKEN = "7507929565:AAEgqrkHim1mVY-hvdcToSQqIfGOAJJwfTo"
bot = Bot(TOKEN)

async def main():
    print(f'Bot {bot}')
    # Message Trojan
    try:
        msg = await bot.send_message(chat_id="@solana_trojanbot", text="hi from ye_tracker")
        print(f"Sent to Trojan, Chat ID: {msg.chat_id}")
    except Exception as e:
        print(f"Error sending to Trojan: {e}")
    # Get updates
    updates = await bot.get_updates()
    print(f'Updates {updates}')
    for update in updates:
        print(f"Chat ID: {update.message.chat_id} | Text: {update.message.text}")

if __name__ == "__main__":
    asyncio.run(main())