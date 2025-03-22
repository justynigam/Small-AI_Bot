from http.client import responses
import torch
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from sympy.strategies.branch import chain
from transformers import pipeline


model = pipeline("text-generation" ,
                 model="mistralai/Mistral-7B-Instruct-v0.1",
                 device="cpu",
                 max_length = 256,
                 truncation = True,)

llm = HuggingFacePipeline(pipeline=model)

template = PromptTemplate.from_template("Explain {topic} in detail for a {age} year old to understand .")
chain = template | llm
topic =  input("Topic : ")
age = input("Age :")

response = chain.invoke({"topid": topic , "age": age})
print(response)

#model = pipeline("summarization", model="facebook/bart-large-cnn" , device="cpu")
#response = model("Machine learning is a fascinating field of artificial intelligence that allows computers to learn from data and improve their performance over time without being explicitly programmed. Essentially, it’s about teaching machines to recognize patterns, make predictions, or take actions based on examples rather than hard-coded rules.There are a few main types of machine learning:Supervised Learning: The machine is trained on a labeled dataset, meaning it’s given inputs paired with the correct outputs. For example, if you’re teaching a model to recognize cats in photos, you’d provide it with images labeled cat or not cat. It learns to map inputs to outputs and can then predict labels for new, unseen data.Unsupervised Learning: Here, the machine gets unlabeled data and has to find patterns or structure on its own. Think clustering customers into groups based on shopping habits without telling it what those groups mean.Reinforcement Learning: This is more like teaching a dog a trick. The machine interacts with an environment, takes actions, and learns by receiving rewards or penalties. It’s how something like a game-playing AI figures out the best moves to win.")
#print(response)