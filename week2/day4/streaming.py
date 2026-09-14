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
prompt="what is internet. explain in 200 words"
message={
    "role":"user",
    "content":prompt
}
messages=[message]
# response=client.chat.completions.create(model=model,messages=messages)
# content = response.choices[0].message.content
# print(content)

stream=client.chat.completions.create(model=model, messages=messages, stream=True)

for chunck in stream:
    content=chunck.choices[0].delta.content
    if content:
        print(content, end="", flush=True)