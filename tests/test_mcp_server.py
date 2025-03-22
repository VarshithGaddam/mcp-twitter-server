import unittest
from src.mcp_server import MCPServer
from src.twitter_client import TwitterClient
from src.context_manager import ContextManager
import json
from flask import Flask

class TestMCPServer(unittest.TestCase):
    def setUp(self):
        # Initialize a test Flask app and server with shared ContextManager
        self.twitter_client = TwitterClient()
        self.context_manager = ContextManager()
        self.server = MCPServer(self.twitter_client, host="localhost", port=8081, context_manager=self.context_manager)
        self.app = self.server.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_root_endpoint(self):
        response = self.client.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {"message": "Welcome to MCP Twitter Server! Use /mcp/context for API calls."})

    def test_fetch_tweet(self):
        payload = {"action": "fetch_tweet", "tweet_id": "123"}
        response = self.client.post('/mcp/context', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["data"]["tweet_id"], "123")
        self.assertIn("text", data["data"])
        self.assertIn("author", data["data"])
        self.assertIn("created_at", data["data"])

    def test_fetch_tweet_missing_id(self):
        payload = {"action": "fetch_tweet"}
        response = self.client.post('/mcp/context', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["message"], "Missing tweet_id")

    def test_search_tweets(self):
        payload = {"action": "search_tweets", "query": "python"}
        response = self.client.post('/mcp/context', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["data"]["query"], "python")
        self.assertTrue(isinstance(data["data"]["results"], list))
        self.assertGreaterEqual(len(data["data"]["results"]), 1)

    def test_search_tweets_missing_query(self):
        payload = {"action": "search_tweets"}
        response = self.client.post('/mcp/context', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["message"], "Missing query")

    def test_get_context(self):
        self.context_manager.update_context("test_key", {"test": "data"})
        payload = {"action": "get_context", "key": "test_key"}
        response = self.client.post('/mcp/context', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["data"], {"test": "data"})

    def test_get_context_missing_key(self):
        payload = {"action": "get_context"}
        response = self.client.post('/mcp/context', json=payload)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "error")
        self.assertEqual(data["message"], "Missing key")

if __name__ == "__main__":
    unittest.main()
