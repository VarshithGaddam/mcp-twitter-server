from src.mcp_server import MCPServer  # Absolute import
from src.twitter_client import TwitterClient  # Absolute import
from src.utils import load_config  # Absolute import
import os

def main():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    config = load_config(config_path)
    twitter_client = TwitterClient()
    server = MCPServer(twitter_client, host=config["server"]["host"], port=config["server"]["port"])
    server.run()

if __name__ == "__main__":
    main()
