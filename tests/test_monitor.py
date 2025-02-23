# tests/test_monitor.py
import unittest
from src.twitter_monitor import TwitterMonitor

class TestMonitor(unittest.TestCase):
    def test_address_detection(self):
        # Mock tweet and callback
        def mock_callback(addr): self.detected = addr
        monitor = TwitterMonitor(mock_callback)
        tweet = type('Tweet', (), {'author_id': 169686021, 'text': 'YeCoin CA: Fk2bN5eY8J9KQwL7mRt4P3sT6VcX'})()
        monitor.on_tweet(tweet)
        self.assertEqual(self.detected, 'Fk2bN5eY8J9KQwL7mRt4P3sT6VcX')

if __name__ == '__main__':
    unittest.main()