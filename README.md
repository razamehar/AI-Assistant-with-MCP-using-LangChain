# AI Assistant with MCP using LangChain

An interactive AI assistant powered by **LangChain**, **OpenAI**, and **Model Context Protocol (MCP)**. This assistant supports persistent memory, file system access, and web-based tasks using MCP agents.

This assistant uses **MCP servers** to interact with both:
- **Airbnb** (to search listings)
- **Local filesystem** (to read/write files)
---

## Features

- Conversational AI assistant with memory  
- Integrates LangChain's `ChatOpenAI` model  
- Uses MCP to interact with:
  - Airbnb website data
  - Local filesystem
- Custom command support: `exit`, `quit`, `clear`
- Can write responses to local files

---

## Tech Stack

- Python 3.10+
- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/)
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol)
- Node.js (for running MCP servers)
- Asyncio for non-blocking I/O

---

## Project Structure

AI Assistant with MCP using LangChain/
```bash
│
├── app.py                # Main script to run the assistant
├── browser_mcp.json      # MCP configuration (Airbnb + Filesystem)
├── .env                  # Store your OpenAI API key here
└── README.md             # This file
```

## Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-assistant-mcp.git
cd ai-assistant-mcp
```

2. Install Node.js
Make sure Node.js is installed on your system. You can download it from nodejs.org.

3. Install Python Dependencies using uv
```bash
pip install uv
uv init "AI Assistant with MCP using LangChain"
uv add dotenv langchain-openai
```

Alternatively, use pip:
```bash
pip install python-dotenv langchain-openai
```

4. Add .env File
```ini
OPENAI_API_KEY=your_openai_api_key
```
5. Run the Assistant
```bash
uv run app.py
```

If you encounter a warning like this:
```r
warning: `VIRTUAL_ENV=C:\Users\...\` does not match the project environment path `.venv`
```

You can ignore it or run with:
```bash
uv --active run app.py
```

## Sample Interaction
```pgsql
===== Interactive MCP Chat =====
Type 'exit' or 'quit' to end the conversation
Type 'clear' to clear conversation history
==================================

You: Top hotels in Berlin under 100 euros per night and then write the result in a file called hotels.txt

Assistant: I have compiled the top hotels in Berlin under 100 euros per night and saved the information in a file named "hotels.txt".
```

This will automatically create a file hotels.txt in your local directory with the assistant's response.

## Available Commands in Chat
- exit or quit → Ends the session
- clear → Clears conversation memory

## MCP Configuration (browser_mcp.json)
This configuration enables two MCP servers:
- Airbnb MCP Server (for browsing listings)
- Filesystem MCP Server (for reading/writing local files)
Update the local path in the filesystem config to match your environment.

## Notes
- You must have Node.js installed to run MCP servers.
- This assistant supports memory through MCPAgent(memory_enabled=True).
- You can add more MCP servers to browser_mcp.json as needed.

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com].