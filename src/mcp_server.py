from flask import Flask, request, jsonify
from .context_manager import ContextManager  # Relative import

class MCPServer:
    def __init__(self, twitter_client, host="0.0.0.0", port=8081, context_manager=None):
        self.app = Flask(__name__)
        self.twitter_client = twitter_client
        self.context_manager = context_manager if context_manager is not None else ContextManager()
        self.host = host
        self.port = port
        self._register_routes()

    def _register_routes(self):
        @self.app.route("/mcp/context", methods=["POST"])
        def handle_context():
            data = request.json
            action = data.get("action")
            if action == "fetch_tweet":
                tweet_id = data.get("tweet_id")
                if not tweet_id:
                    return jsonify({"status": "error", "message": "Missing tweet_id"})
                result = self.twitter_client.get_tweet(tweet_id)
                self.context_manager.update_context(tweet_id, result)
                return jsonify({"status": "success", "data": result})
            elif action == "search_tweets":
                query = data.get("query")
                if not query:
                    return jsonify({"status": "error", "message": "Missing query"})
                result = self.twitter_client.search_tweets(query)
                self.context_manager.update_context(query, result)
                return jsonify({"status": "success", "data": result})
            elif action == "get_context":
                key = data.get("key")
                if not key:
                    return jsonify({"status": "error", "message": "Missing key"})
                result = self.context_manager.get_context(key)
                return jsonify({"status": "success", "data": result})
            return jsonify({"status": "error", "message": "Invalid action"})

        @self.app.route("/", methods=["GET"])
        def home():
            return jsonify({"message": "Welcome to MCP Twitter Server! Use /mcp/context for API calls."})

    def run(self):
        self.app.run(host=self.host, port=self.port)
