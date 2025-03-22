# MCP Twitter Server with OpenAI Integration

This project implements a **Model Context Protocol (MCP)** server to enable an AI assistant, powered by OpenAI, to interact with a mock Twitter/X API. It fulfills the internship assignment requirement to integrate an AI agent like Claude (using OpenAI instead) with an application. The server simulates Twitter functionality, processes responses with OpenAI’s GPT-3.5-turbo, and includes unit tests for reliability.

## Features
- **Fetch Tweet by ID**: Retrieve a mock tweet using a specified ID.
- **Search Tweets by Query**: Search for mock tweets based on a keyword.
- **Context Management**: Store and retrieve data for AI continuity.
- **OpenAI Integration**: Analyze server responses using OpenAI’s API (or a mock fallback).
- **Unit Tests**: Verify server and mock Twitter client functionality.

## Project Structure
mcp-twitter-server/ ├── src/ # Source code │ ├── main.py # Server entry point │ ├── mcp_server.py # MCP server with API endpoints │ ├── twitter_client.py # Mock Twitter API client │ ├── openai_agent.py # OpenAI agent for interaction │ ├── context_manager.py # Context storage for AI │ └── utils.py # Configuration loader ├── config/ # Configuration │ └── config.yaml # Server settings (host, port) ├── tests/ # Unit tests │ ├── test_mcp_server.py # Tests for MCPServer │ └── test_twitter_client.py # Tests for TwitterClient ├── docs/ # Documentation │ ├── README.md # This file │ └── demo_slides.pdf # Demo presentation (optional) ├── requirements.txt # Python dependencies └── .gitignore # Files to exclude from git

bash
Copy

## Prerequisites
- Python 3.10 or higher
- Git
- Terminal (e.g., Command Prompt on Windows)
- OpenAI API key (optional; mock mode available)

## Setup Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/VarshithGaddam/mcp-twitter-server.git
cd mcp-twitter-server
2. Create Virtual Environment:
bash
Copy
python -m venv venv
Windows: venv\Scripts\activate

Linux/MacOS: source venv/bin/activate

###3.Install Dependencies:

pip install -r requirements.txt
###4. Run the Server:
python src/main.py
Server runs on http://localhost:8081.

OpenAI Integration
The project uses OpenAI’s GPT-3.5-turbo to process server responses (src/openai_agent.py).

#Running the OpenAI Agent
Set your OpenAI API key (get it from platform.openai.com):

set OPENAI_API_KEY=your-api-key-here
Start the server (in one terminal):
python src/main.py
Run the agent (in another terminal):


python src/openai_agent.py
This will fetch tweet "123", search for "python", and retrieve context. Without an API key, it uses a mock OpenAI.

###Testing
Unit tests ensure functionality:

tests/test_mcp_server.py: Tests server endpoints.

tests/test_twitter_client.py: Tests mock Twitter data.

###Running Tests:
python -m unittest tests/test_mcp_server.py
python -m unittest tests/test_twitter_client.py

#Why Mock Implementation?
Twitter API: Mocked to avoid costs and limits associated with using the real Twitter API.

OpenAI: Supports real API with a key; defaults to mock for free usage.

Submission Notes
AI Choice: Used OpenAI instead of Claude due to the availability of a free tier.
Next Steps: Feedback on adding real Twitter API or more features is welcome.

Contact: Reach me at varshithg2004@gmail.com for questions.

License
For educational purposes only.
