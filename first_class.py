# pip install python-dotenv
import os
from dotenv import load_dotenv
# pip install openai
from openai import OpenAI
load_dotenv()                 # loads everything from .env


#client = OpenAI()   # reads your API key from the environment

# using GROQ API key from .env
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a witty travel guide."},
#         {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
#     ],
# )

response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Bangalore."},
    ],
)
print(response.choices[0].message.content)


# now OpenAI() finds the key automatically — no key in your code 🎉