# src/twitter_monitor.py
import tweepy
from config.config import Config

class TwitterMonitor(tweepy.StreamingClient):
    def __init__(self, callback):
        super().__init__(Config.BEARER_TOKEN)
        self.callback = callback

    def on_tweet(self, tweet):
        if tweet.author_id == Config.KANYE_USER_ID:
            print(f"Tweet: {tweet.text}")
            match = re.search(Config.ADDRESS_PATTERN, tweet.text)
            if match:
                address = match.group(0)
                print(f"Found Solana address: {address}")
                self.callback(address)

    def on_error(self, status):
        print(f"Error: {status}")

def start_monitor(callback):
    monitor = TwitterMonitor(callback)
    print(f'Monitor: {monitor}')
    print("Adding rule...")
    response = monitor.add_rules(tweepy.StreamRule("from:ye"))
    print(f"Rule response: {response}")
    monitor.filter()