import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"


def llm_ans(prompt):
    message={
        "role":"user",
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans




bad_prompt="""
#ROLE:
# You are a support assistant at a mobile/laptop company
This is a user complaint
My laptp is not working
classify this  
"""

good_prompt=""" 
#ROLE:
You are a support assistant at a mobile/laptop company.
#TASK:
Your have to classify the issue in a category.
#CONSTRAINT:
You have to classify the issue in one of the three category
namely Billing, Tehnical and Refund
#OUTPUT FORMAT:
Your answer should be one word and should be one of the categories from the given constraint

#EXAMPLE:
for instance if he/she want a refund then its refund.

#FALLBACK:
If the issue is unrealted to any of the categories mentioned in the contraint then return Other.
This is a user complaint
My laptop is not working"""
print(llm_ans(good_prompt))