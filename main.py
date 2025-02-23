# main.py
from src.twitter_monitor import start_monitor
from src.telegram_client import buy_token
from src.token_validator import validate_token  # Optional

def handle_address(address):
    if validate_token(address):  # Optional check
        buy_token(address)
    else:
        print(f"Skipping invalid token: {address}")

if __name__ == "__main__":
    print("Starting Kanye sniper...")
    start_monitor(handle_address)