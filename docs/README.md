🚀 MCP Twitter Server (Mock Implementation)
This project implements a Model Context Protocol (MCP) server that enables an AI assistant (e.g., Claude, ChatGPT) to interact with a mock Twitter/X API. It simulates Twitter functionality without requiring real API credentials, making it a cost-free solution for demonstration purposes.

🔥 Features
✅ #FetchTweetByID – Simulates retrieving a tweet using a given ID.
✅ #SearchTweetsByQuery – Simulates searching tweets based on a keyword or phrase.
✅ #ContextManagement – Stores and retrieves API response data for AI interaction continuity.

📂 #ProjectStructure
graphql
Copy
Edit
mcp-twitter-server/
├── src/                    # Source code  
│   ├── main.py             # Server entry point  
│   ├── mcp_server.py       # MCP server with API endpoints  
│   ├── twitter_client.py   # Mock Twitter API client  
│   ├── context_manager.py  # Context storage for AI  
│   └── utils.py            # Configuration loader  
├── config/                 # Configuration  
│   └── config.yaml         # Server settings (host, port)  
├── docs/                   # Documentation  
│   ├── README.md           # This file  
│   └── demo_slides.pdf     # Demo presentation (or video link)  
├── requirements.txt        # Python dependencies  
└── .gitignore              # Files to exclude from git  
🛠 #Prerequisites
#Python 3.6 or higher
#Git (for cloning the repository)
#Terminal (e.g., Command Prompt, Bash)
⚡ #Installation & Setup
1️⃣ #CloneTheRepo
bash
Copy
Edit
git clone https://github.com/yourusername/mcp-twitter-server.git  
cd mcp-twitter-server  
(Replace yourusername with your GitHub username.)

2️⃣ #CreateVirtualEnv
bash
Copy
Edit
python -m venv venv  
# Activate it:
# Windows: 
venv\Scripts\activate  
# Linux/MacOS:
source venv/bin/activate  
3️⃣ #InstallDependencies
bash
Copy
Edit
pip install -r requirements.txt  
4️⃣ #RunTheServer
bash
Copy
Edit
python src/main.py  
📌 The server starts at http://localhost:8081
Expected Output:

csharp
Copy
Edit
 * Running on http://127.0.0.1:8081  
 * Running on http://[your-local-ip]:8081  
🔗 #Usage (API Requests)
📝 #FetchTweet
bash
Copy
Edit
curl -X POST http://localhost:8081/mcp/context -H "Content-Type: application/json" -d "{\"action\": \"fetch_tweet\", \"tweet_id\": \"123\"}"
📌 Response:

json
Copy
Edit
{
  "status": "success",
  "data": {
    "tweet_id": "123",
    "text": "This is a mock tweet with ID 123!",
    "author": "user2",
    "created_at": "2025-03-16 18:00:00"
  }
}
🔍 #SearchTweets
bash
Copy
Edit
curl -X POST http://localhost:8081/mcp/context -H "Content-Type: application/json" -d "{\"action\": \"search_tweets\", \"query\": \"python\"}"
📌 Response:

json
Copy
Edit
{
  "status": "success",
  "data": {
    "query": "python",
    "results": [
      {
        "tweet_id": "4567",
        "text": "Mock result for 'python': AI 42",
        "author": "mockbot",
        "created_at": "2025-03-16 18:00:01"
      }
    ]
  }
}
🗂 #GetContext
bash
Copy
Edit
curl -X POST http://localhost:8081/mcp/context -H "Content-Type: application/json" -d "{\"action\": \"get_context\", \"key\": \"123\"}"
📌 Response (after fetching tweet 123):

json
Copy
Edit
{
  "status": "success",
  "data": {
    "tweet_id": "123",
    "text": "This is a mock tweet with ID 123!",
    "author": "user2",
    "created_at": "2025-03-16 18:00:00"
  }
}
🌍 #RootEndpoint
Visit http://localhost:8081/ in a browser to see:

json
Copy
Edit
{"message": "Welcome to MCP Twitter Server! Use /mcp/context for API calls."}
🎥 #Demo
📌 A demo is available in docs/demo_slides.pdf (or a video link: [insert link here]).

🤖 #WhyMockImplementation?
This project uses a mock TwitterClient to simulate Twitter API responses, avoiding the need for paid API access. The code is structured to easily integrate with a real Twitter API (e.g., using tweepy) by replacing twitter_client.py with authentic API calls if credentials are available.

🔌 #ExtendingToRealTwitterAPI
To use the real Twitter API:
1️⃣ Obtain credentials from the Twitter Developer Portal.
2️⃣ Install Tweepy:

bash
Copy
Edit
pip install tweepy  
3️⃣ Update twitter_client.py with real API calls.
4️⃣ Add credentials to config.yaml.

🔖 #Notes
✅ Built and tested on Windows (port 8081 to avoid conflicts).
✅ Designed for internship assignments to demonstrate MCP functionality.
✅ No external API costs incurred.

📜 #License
This project is for educational purposes only and not licensed for production use.