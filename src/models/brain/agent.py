from langchain_ollama import ChatOllama

agent = ChatOllama(
    model="deepseek-r1:7b",
    temperature=0
)