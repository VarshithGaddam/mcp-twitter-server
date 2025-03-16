import unittest
from src.twitter_client import TwitterClient

class TestTwitterClient(unittest.TestCase):
    def setUp(self):
        self.client = TwitterClient("mock_key")

    def test_get_tweet(self):
        result = self.client.get_tweet("123")
        self.assertEqual(result["tweet_id"], "123")
        self.assertIn("Mock tweet content", result["text"])

    def test_search_tweets(self):
        result = self.client.search_tweets("test_query")
        self.assertEqual(result["query"], "test_query")
        self.assertEqual(len(result["results"]), 2)

if __name__ == "__main__":
    unittest.main()