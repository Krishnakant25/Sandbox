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




**DAY 06:** What I Learned:

** Categorical Encoding (scikit-learn) **

-- Label Encoding: Converted text labels into integers ($0, 1, 2, \dots$) using LabelEncoder.

-- One-Hot Encoding (OHE): Created binary columns for nominal data to prevent models from assuming a mathematical rank between categories.

** Web-Based AI OrchestrationStreamlit UI:**

-- Built a browser-based interface for the chatbot using st.chat_message and st.chat_input.

-- Session Persistence: Managed st.session_state to maintain chat_history and AI memory across web reruns.

-- State Control: Implemented a "Clear-Chat" feature to reset the SystemMessage and conversation history.




**DAY 07:** what I Learned:

** Advanced Preprocessing (scikit-learn) **

-- Mixed Data Workflows: Implemented simultaneous scaling and encoding for datasets with both numerical and categorical variables.

-- Automated Column Selection: Used select_dtypes to isolate features for processing, streamlining pipelines for large-scale data.

** Model Regularization **

-- Lasso (L1) Regression: Applied L1 regularization to perform feature selection by shrinking less important coefficients to zero.

-- Ridge (L2) Regression: Used L2 regularization to prevent overfitting by penalizing the magnitude of coefficients.

** LangChain Orchestration (LCEL) **

-- Chain Composition: Mastered the | (pipe) operator to link ChatPromptTemplate, ChatOpenAI, and StrOutputParser.

-- Modular Logic: Built reusable chains that dynamically inject variables like {animal} and {fact_count} for context-aware responses.




**DAY 08:** what I Learned:
** Advanced Linear Modeling (scikit-learn) **

-- Elastic Net Regularization: Implemented ElasticNet logic within LogisticRegression to combine the feature selection of Lasso (L1) with the stability of Ridge (L2).

-- Classification Metrics: Evaluated loan approval predictions using Accuracy, Precision, Recall, and F1-Score to quantify model performance beyond simple error rates.

-- Feature Engineering: Integrated StandardScaler for continuous variables and OneHotEncoder for categorical data, using np.concatenate to build the final feature matrix.

** LangChain Deep Dive (LCEL Architecture) **

-- Runnable Components: Mastered the use of RunnableLambda to wrap custom Python functions into pipeline-compatible steps.

-- Explicit Sequences: Built structured workflows using RunnableSequence to explicitly define the format_prompt -> invoke_model -> parse_output lifecycle.

-- State Transformation: Learned to handle object transitions, such as converting formatted prompts to message lists using .to_messages() before model invocation.




**DAY 09** what I Learned:

** Supervised Learning (scikit-learn) **

-- Decision Tree Architecture: Mastered the logic of tree-based models that use "if-then-else" decision rules to classify data.

-- Model Validation: Learned to interpret Precision vs. Recall trade-offs in classification, ensuring the model's reliability beyond simple accuracy.

** Advanced LangChain (Sequential Chains) **

-- Output-Input Piping: Implemented sequential logic where the AI performs a primary task (translation) before executing a dependent secondary task (fact expert).

-- Context Preservation: Learned to pass dynamic variables across multiple chain links, allowing for complex, multi-turn AI workflows in a single invoke() call.




**DAY 10** what I Learned:

** Regression with Trees (scikit-learn) **

-- Decision Tree Regressor: Learned how trees handle continuous targets by splitting data into nodes representing mean numerical values rather than discrete classes.

-- Standardization: Applied StandardScaler to ensure numerical inputs are properly normalized before fitting the regressor.

** Concurrent LangChain (Parallel Chains) **

-- RunnableParallel: Mastered executing multiple LLM branches at the exact same time, effectively cutting total wait time in half.

-- Branching Logic: Split a single user input into specialized sub-tasks and aggregated their results into a structured, unified final output.