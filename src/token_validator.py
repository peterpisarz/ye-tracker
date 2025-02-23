# src/token_validator.py
import requests

def validate_token(address):
    url = f"https://api.dexscreener.com/latest/dex/tokens/{address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("pairs") and data["pairs"][0].get("liquidity"):
                print(f"Token {address} has liquidity: {data['pairs'][0]['liquidity']}")
                return True
        return False
    except Exception as e:
        print(f"Validation error: {e}")
        return False