import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"    # Fast Llama model
role="user"
prompt="Suggest me a name for my food comapny in one word"

# SYSTEM_ROLE
message_system={
    "role":"system",
    "content":"You are my brand manager who suggest a name for food company"
}

message={
    "role":role,
    "content":prompt
}
# Temperate by default is 0 means safe
messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,temperature=1)
content = response.choices[0].message.content
print(content)