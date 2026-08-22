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

# # PROMPT FOR UINDERSTANDING TOKENS
prompt1="Hi!"
prompt2="Explain time travel  in detail"
prompt3="Write an essay on machine learing of 1000 words"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
    "role":role,
    "content":prompt
}
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages,max_tokens=50)
    usage=response.usage
    print(f" Prompt: {prompt} ---> Your_tokens:{usage.prompt_tokens}, Completion_tokens:{usage.completion_tokens} : Finish_Reason:{response.choices[0].finish_reason}")