# config/config.py
class Config:
    # X API
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIT8zQEAAAAAXGZ2M8x1JyMsDSpVlHTrJCueM6M%3Dbs8kbsrHn5P3pxZMiNlCpNQi8gQMpmbZEAqckiJQPBBA0tWnMu"
    KANYE_USER_ID = 169686021  # @ye’s user ID

    # Telegram API
    TELEGRAM_TOKEN = "7507929565:AAEgqrkHim1mVY-hvdcToSQqIfGOAJJwfTo" # @ye_tracker_bot
    TROJAN_CHAT_ID = "solana_trojanbot"  # e.g., "-123456789"

    # Sniping settings
    BUY_AMOUNT = 0.3  # SOL amount to spend
    ADDRESS_PATTERN = r"[A-HJ-NP-Za-km-z1-9]{44,58}"  # Solana address regex

    # curl -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAIT8zQEAAAAAXGZ2M8x1JyMsDSpVlHTrJCueM6M%3Dbs8kbsrHn5P3pxZMiNlCpNQi8gQMpmbZEAqckiJQPBBA0tWnMu" "https://api.twitter.com/2/users/169686021"