**DAY 01:** What I Learned:

LangChain Basics: Used SystemMessage to set an AI persona and HumanMessage for user queries.

Reasoning Models: Discovered that gpt-5-nano needs higher max_completion_tokens because it uses tokens to "think" (reasoning) before answering.

Git Workflow: Mastered git init, config, add, commit, and push to sync local code with GitHub.

Security: Set up a .gitignore file to keep my .env (API keys) and venv private.



**DAY 02:** What I learned:

A Python MCP server with 8 tools that lets AI models analyze data — load CSVs, profile data, detect outliers, run SQL, generate charts, and run statistical tests.

**What I Built:** A Python MCP server with 8 tools (load data, profile, detect outliers, run SQL, generate charts, hypothesis tests) that lets AI models analyze data conversationally.

**What I Learned:**
- **MCP Protocol:** Structured way for AI to call external tools over stdio — think of it as giving AI "hands" to touch your data
- **Claude Desktop:** MCP tools need a Pro plan — used MCP Inspector (free browser UI) for testing instead
- **Windows Gotcha:** Spaces in your username (`Krishna Kant Sahu`) silently break config paths — always use full absolute paths
- **uv:** Much faster than pip for managing Python environments and packages

**Next Steps:** Connect Gemini AI for free conversational analysis, add FastAPI frontend, test with PostgreSQL
