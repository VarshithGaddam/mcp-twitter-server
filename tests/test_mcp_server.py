import unittest
from src.mcp_server import MCPServer
from src.twitter_client import TwitterClient

class TestMCPServer(unittest.TestCase):
    def setUp(self):
        self.twitter_client = TwitterClient("mock_key")
        self.server = MCPServer(self.twitter_client)
        self.app = self.server.app.test_client()

    def test_fetch_tweet(self):
        response = self.app.post("/mcp/context", json={"action": "fetch_tweet", "tweet_id": "123"})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["data"]["tweet_id"], "123")

    def test_missing_tweet_id(self):
        response = self.app.post("/mcp/context", json={"action": "fetch_tweet"})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "error")

if __name__ == "__main__":
    unittest.main()