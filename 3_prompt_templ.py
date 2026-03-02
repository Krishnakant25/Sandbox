from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature=0.9)

sys_prompt_template = PromptTemplate.from_template("""Answer the following question using the given
                                                   Context: {context}
                                                   Question: {question}""")

sys_prompt = sys_prompt_template.invoke({
    "context": "The capital of India is New Delhi.",
    "question": "What is the capital of france?"
})

response = model.invoke(sys_prompt)
print(response.content)