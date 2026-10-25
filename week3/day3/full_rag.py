import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2") #384

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
groq_model="openai/gpt-oss-120b"

documents = [
    "Employees receive 24 days of paid leave per year.",
   
    "Employees work from the office on Tuesday, Wednesday and Thursday. "
    "Monday and Friday are optional work-from-home days.",
   
    "Employees receive Rs 3000 per month for gym reimbursement.",
   
    "Employees can claim Rs 2000 per month for home internet.",
   
    "Employees have a 90 day notice period."
]
document_embedding=model.encode(documents)
def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
    

def retrive(qembedding):
    scores = []
    for i, document in enumerate(document_embedding):
        score = cosine_similarity(qembedding, document)
        scores.append((score, documents[i]))
    scores.sort(reverse=True)
    return scores[0]


def ask_llm(question,context):
    
    sys_prompt=f"""answe in one line and anwer based on the given context{context} and do not hallucinate"""
    system_message={
        "role":"system",
        "content":sys_prompt
    }
    message={
        "role":"user",
        "content":question
    }
    messages=[system_message,message]
    response=client.chat.completions.create(model=groq_model,messages=messages)
    answer=response.choices[0].message.content
    return answer

           

query="Whats my PTO situation looking like?"
qembedding=model.encode(query)
score,context=retrive(qembedding)
print(score)
answer=ask_llm(query,context)
print(answer)


