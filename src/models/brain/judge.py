from langchain_ollama import ChatOllama

judge = ChatOllama(
    model="gemma4:12b",
    temperature=0,
    keep_alive=0,
)