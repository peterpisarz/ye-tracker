from telegram import Bot
from telegram.error import TelegramError

TOKEN = "7507929565:AAEgqrkHim1mVY-hvdcToSQqIfGOAJJwfTo"
# Guess Trojan’s public chat or use a temp ID if you know it
TEMP_TROJAN_ID = "-1001234567890"  # Replace if you’ve got a hunch

bot = Bot(TOKEN)
try:
    bot.send_message(chat_id=TEMP_TROJAN_ID, text="hi from @ye_tracker_bot")
    print("Message sent to Trojan")
except TelegramError as e:
    print(f"Error: {e}")