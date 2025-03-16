from mcp_server import MCPServer
from twitter_client import TwitterClient
from utils import load_config

def main():
    config = load_config("config/config.yaml")
    twitter_client = TwitterClient()  # No API key for mock
    server = MCPServer(twitter_client, host=config["server"]["host"], port=config["server"]["port"])
    server.run()

if __name__ == "__main__":
    main()