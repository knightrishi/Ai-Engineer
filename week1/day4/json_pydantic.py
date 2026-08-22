import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"    # Fast Llama model
role="user"

# STructuring the data
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f""" Extract the Personal information strictly based on the schema and give me a json output based on {schema}"""

message_system={
    "role":"system",
    "content":system_prompt

}

text="Hello my name is Arnav Singh and i have having an issue with my CosmicByte Dragonfly keybord.My address is Bhopal. My contact number is 987650> i like my keybord very much.please repair it. My email is:abc@gmail.com"

prompt=f"""This is a customer ticket please extract person information from this {text}"""
message={
    "role":role,
    "content":prompt
}
messages=[message_system,message]
response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)
ans = response.choices[0].message.content
print(ans)


# How to read JSON DAT
import json
raw_json=ans
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)