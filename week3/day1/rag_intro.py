import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"

#step 1 in RAG
knowledge_base={
    "age":"The age of Pratyush Narain is 25",
    "net worth":"Newt worth of Pratyush is 20000"

}
#step 2-- retrival
def retrive_info(question):
    questions=question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "net worth" in question:
        return knowledge_base["net worth"]
    else:
        return None


def ask_llm(question):
    context=retrive_info(question)
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
    response=client.chat.completions.create(model=model,messages=messages)
    answer=response.choices[0].message.content
    return answer

question="What is age pratyush "

print(ask_llm(question))