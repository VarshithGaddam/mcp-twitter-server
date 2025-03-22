import unittest
from src.twitter_client import TwitterClient
from datetime import datetime

class TestTwitterClient(unittest.TestCase):
    def setUp(self):
        self.client = TwitterClient()

    def test_get_tweet(self):
        # Test fetching a tweet
        tweet = self.client.get_tweet("123")
        self.assertEqual(tweet["tweet_id"], "123")
        self.assertIn(tweet["text"], [f"This is a mock tweet with ID 123! {word}" for word in self.client.mock_words])
        self.assertIn(tweet["author"], self.client.mock_users)
        # Check if created_at is a valid datetime string
        try:
            datetime.strptime(tweet["created_at"], "%Y-%m-%d %H:%M:%S")
            valid_datetime = True
        except ValueError:
            valid_datetime = False
        self.assertTrue(valid_datetime)

    def test_search_tweets(self):
        # Test searching tweets
        result = self.client.search_tweets("python")
        self.assertEqual(result["query"], "python")
        self.assertTrue(isinstance(result["results"], list))
        self.assertGreaterEqual(len(result["results"]), 1)
        self.assertLessEqual(len(result["results"]), 3)
        for tweet in result["results"]:
            self.assertTrue(isinstance(tweet["tweet_id"], str))
            self.assertIn("python", tweet["text"])
            self.assertIn(tweet["author"], self.client.mock_users)
            try:
                datetime.strptime(tweet["created_at"], "%Y-%m-%d %H:%M:%S")
                valid_datetime = True
            except ValueError:
                valid_datetime = False
            self.assertTrue(valid_datetime)

if __name__ == "__main__":
    unittest.main()
