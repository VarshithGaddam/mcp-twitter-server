import random
from datetime import datetime

class TwitterClient:
    def __init__(self, api_key=None):  # api_key ignored for mock
        self.mock_users = ["user1", "user2", "user3", "mockbot"]
        self.mock_words = ["hello", "world", "python", "AI", "coding"]

    def get_tweet(self, tweet_id):
        return {
            "tweet_id": tweet_id,
            "text": f"This is a mock tweet with ID {tweet_id}! {random.choice(self.mock_words)}",
            "author": random.choice(self.mock_users),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def search_tweets(self, query):
        results = [
            {
                "tweet_id": str(random.randint(1000, 9999)),
                "text": f"Mock result for '{query}': {random.choice(self.mock_words)} {random.randint(1, 100)}",
                "author": random.choice(self.mock_users),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            for _ in range(random.randint(1, 3))  # 1-3 results
        ]
        return {"query": query, "results": results} 
