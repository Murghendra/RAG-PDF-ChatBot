from langchain_community.llms import Ollama

llm = Ollama(model="phi")

response = llm.invoke("give me 10 interesting facts about space")

print(response)