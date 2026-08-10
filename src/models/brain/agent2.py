from langchain_ollama import ChatOllama

agent2 = ChatOllama(
    model="mistral:7b",
    temperature=0
)