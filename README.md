**DAY 01:** What I Learned:

-- LangChain Basics: Used SystemMessage to set an AI persona and HumanMessage for user queries.

-- Reasoning Models: Discovered that gpt-5-nano needs higher max_completion_tokens because it uses tokens to "think" (reasoning) before answering.

-- Git Workflow: Mastered git init, config, add, commit, and push to sync local code with GitHub.

-- Security: Set up a .gitignore file to keep my .env (API keys) and venv private.



**DAY 02:** What I learned:

** LangChain Architecture **

-- Prompt Engineering: Implemented PromptTemplate and SystemMessage to define specific AI personas, ensuring context-aware and consistent model behavior.

-- LCEL Implementation: Transitioned from manual invocations to modular chains using LangChain Expression Language (template | model) for cleaner, automated logic flows.

** Reasoning Model Optimization **

-- Technical Discovery: Identified that gpt-5-nano requires a significantly higher max_completion_tokens budget compared to standard models.

-- Mechanism: Noted that these models utilize extra tokens for internal "reasoning" or "thinking" steps before delivering the final answer.




**DAY 03:** What i learned:

** Structured Output with Pydantic **

-- Schema Enforcement: Used PydanticOutputParser to strictly control LLM responses by defining a BaseModel schema (title, director, release_date, description).

-- Reliable JSON Generation: Learned how parser.get_format_instructions() guides the model to return valid, structured JSON instead of unpredictable free-text output.

-- Validation Layer: Understood how Pydantic automatically validates and parses the model response into a strongly-typed Python object.

** Prompt Engineering Enhancement **

-- Partial Variables: Injected format_instructions into PromptTemplate using partial_variables to dynamically enforce output structure.




**DAY 04:** What i learned:

** Context-Aware Q&A (LangChain) **

-- Hallucination Prevention: Designed prompts that inject dynamic context alongside queries, strictly forcing the model to rely only on provided facts or safely fallback to "I don't know."

** Multiple Linear Regression (scikit-learn) **

-- Multi-Feature Predictions: Built models using multiple independent variables simultaneously.  Evaluated feature weights (coef_, intercept_) and validated accuracy using MSE, MAE, and R².

** Polynomial Regression (scikit-learn) **

-- Modeling Non-Linearity: Used PolynomialFeatures (degree=2) to successfully fit curved datasets.  Mastered the strict fit_transform (training) vs. transform (testing) pipeline to prevent data leakage.




**DAY 05:** What I Learned:
** LangChain Development **
-- Stateless Batching: Used .batch() to run multiple prompts simultaneously, noting that context does not carry over between individual inputs in the list.
-- Stateful Chat: Built an interactive loop using chat_history to store HumanMessage and AIMessage objects, enabling the AI to remember previous context.
** Machine Learning & Preprocessing **
-- Feature Scaling: Applied StandardScaler to normalize data, ensuring features like Age and Experience are on a consistent scale for the model.
-- Evaluation Metrics: Validated model performance using $R^2$ and Mean Absolute Error (MAE) to measure prediction accuracy.