# MCP Twitter Server with OpenAI Integration

This project implements a **Model Context Protocol (MCP)** server that simulates a Twitter/X API and integrates with an AI agent, powered by OpenAI’s GPT-3.5-turbo, as per the internship assignment requirement to use an AI like Claude. Due to quota limits on my OpenAI account, it currently defaults to a mock OpenAI response, with real API integration available when funded. The server handles tweet fetching, searching, and context management, with unit tests ensuring reliability.

## Features
- **Fetch Tweet by ID**: Retrieve a mock tweet using a specified ID.
- **Search Tweets by Query**: Search for mock tweets based on a keyword.
- **Context Management**: Store and retrieve data for AI continuity.
- **OpenAI Integration**: Analyze responses with OpenAI (mock by default; real with funded key).
- **Unit Tests**: Validate server endpoints and mock Twitter client functionality.

## Project Structure
mcp-twitter-server/ ├── src/ # Source code │ ├── main.py # Server entry point │ ├── mcp_server.py # MCP server with API endpoints │ ├── twitter_client.py # Mock Twitter API client │ ├── openai_agent.py # OpenAI agent (mock/real) │ ├── context_manager.py # Context storage │ └── utils.py # Config loader ├── config/ # Configuration │ └── config.yaml # Server settings ├── tests/ # Unit tests │ ├── test_mcp_server.py # Server endpoint tests │ └── test_twitter_client.py # Mock Twitter client tests ├── docs/ # Documentation │ └── README.md # This file ├── requirements.txt # Dependencies └── .gitignore # Git exclusions

## Prerequisites
- Python 3.10+
- Git
- Terminal (e.g., Command Prompt on Windows)
- OpenAI API key (optional for real API; mock works without)

## Setup Instructions

### 1. Clone the Repository:

git clone https://github.com/VarshithGaddam/mcp-twitter-server.git
cd mcp-twitter-server
Create Virtual Environment:
python -m venv venv
Install Dependencies:
pip install -r requirements.txt
4. Run the Server:
python -m src.main
Server runs on http://localhost:8081.
penAI Integration
The openai_agent.py script processes server responses:

Mock Mode: Default due to quota limits (no key needed).

Real Mode: Enable with a funded OpenAI API key.

Running the OpenAI Agent
Start the Server (one terminal):
python -m src.main
Run the Agent (another terminal)
python src/openai_agent.py
Output: Mock OpenAI responses for fetch_tweet, search_tweets, and get_context.

### For Real OpenAI:
set OPENAI_API_KEY=your-funded-key-here
Edit openai_agent.py, remove False in the if "OPENAI_API_KEY" in os.environ check, then rerun.

### Running Unit Tests
Verify functionality with tests:

### Activate Environment:
venv\Scripts\activate
###Run Server Tests:
python -m unittest tests.test_mcp_server -v
7 tests for endpoints and error handling.

### Run Twitter Client Tests:
python -m unittest tests.test_twitter_client -v
2 tests for mock tweet generation.

### Run All Tests:
python -m unittest discover -s tests -v
Demo Video
A demo video showcasing setup, agent interaction (mock OpenAI), and tests is available at:

Recorded: Server start, agent run, and test execution.

### Why Mock Implementation?
Twitter API: Mocked to avoid real API costs/limits.

OpenAI: Mocked due to quota exhaustion; real API works with funding (see openai_agent.py).

### Dependencies
flask==2.3.2

pyyaml==6.0.1

requests==2.31.0

openai==1.53.0 # Updated for compatibility

werkzeug==2.3.7

### Submission Notes
AI Choice: Used OpenAI (mock) instead of Claude due to quota issues; real integration ready with funding.

GitHub: https://github.com/VarshithGaddam/mcp-twitter-server



### Next Steps
Fund OpenAI account for real API demo.

Add real Twitter API integration if required.

### License
For educational purposes only.

