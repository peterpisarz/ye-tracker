# src/telegram_client.py
from telegram import Bot
from telegram.error import TelegramError
from config.config import Config

class TelegramClient:
    def __init__(self):
        self.bot = Bot(Config.TELEGRAM_TOKEN)

    async def send_buy_command(self, address):
        message = f"/buy {address} {Config.BUY_AMOUNT}"
        try:
            msg = await self.bot.send_message(
                chat_id=Config.TROJAN_CHAT_ID, text=message
            )
            print(f"Sent to Trojan: {message} | Chat ID: {msg.chat_id}")
        except TelegramError as e:
            print(f"Telegram error: {e}")

def buy_token(address):
    import asyncio
    client = TelegramClient()
    asyncio.run(client.send_buy_command(address))