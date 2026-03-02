**DAY 01:** What I Learned:

-- LangChain Basics: Used SystemMessage to set an AI persona and HumanMessage for user queries.

-- Reasoning Models: Discovered that gpt-5-nano needs higher max_completion_tokens because it uses tokens to "think" (reasoning) before answering.

-- Git Workflow: Mastered git init, config, add, commit, and push to sync local code with GitHub.

-- Security: Set up a .gitignore file to keep my .env (API keys) and venv private.



**DAY 02:** What I learned:

*** LangChain Architecture ***

-- Prompt Engineering: Implemented PromptTemplate and SystemMessage to define specific AI personas, ensuring context-aware and consistent model behavior.

-- LCEL Implementation: Transitioned from manual invocations to modular chains using LangChain Expression Language (template | model) for cleaner, automated logic flows.

*** Reasoning Model Optimization ***

-- Technical Discovery: Identified that gpt-5-nano requires a significantly higher max_completion_tokens budget compared to standard models.

-- Mechanism: Noted that these models utilize extra tokens for internal "reasoning" or "thinking" steps before delivering the final answer.
