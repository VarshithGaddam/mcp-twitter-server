import requests
import json
import os
from openai import OpenAI

class MockOpenAI:
    def chat_completions_create(self, prompt):
        return f"Mock OpenAI response to: {prompt}"

class OpenAIAgent:
    def __init__(self, server_url="http://localhost:8081"):
        self.server_url = server_url
        # Force mock for demo
        if "OPENAI_API_KEY" in os.environ and False:  # Always mock
            self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
            print("Using real OpenAI API.")
        else:
            self.client = MockOpenAI()
            print("Using mock OpenAI for demo purposes.")

    def send_request(self, action, params):
        payload = {"action": action}
        payload.update(params)
        response = requests.post(
            f"{self.server_url}/mcp/context",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        return response.json()

    def process_response(self, action, params):
        result = self.send_request(action, params)
        data = result.get("data", "No data returned")
        prompt = f"Analyze this MCP server response for {action}: {json.dumps(data)}"
        if isinstance(self.client, MockOpenAI):
            openai_response = self.client.chat_completions_create(prompt)
        else:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            openai_response = response.choices[0].message.content
        print(f"OpenAI Response for {action}: {openai_response}")
        return result, openai_response

    def fetch_tweet(self, tweet_id):
        print(f"Fetching tweet with ID {tweet_id}")
        return self.process_response("fetch_tweet", {"tweet_id": tweet_id})

    def search_tweets(self, query):
        print(f"Searching tweets for '{query}'")
        return self.process_response("search_tweets", {"query": query})

    def get_context(self, key):
        print(f"Retrieving context for key '{key}'")
        return self.process_response("get_context", {"key": key})

if __name__ == "__main__":
    agent = OpenAIAgent()
    agent.fetch_tweet("123")
    agent.search_tweets("python")
    agent.get_context("123")
