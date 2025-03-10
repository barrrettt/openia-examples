import openai
import os
from dotenv import load_dotenv

client = None

def setup():
    load_dotenv()
    api = os.getenv('OPENAI_API_KEY')
    if api == None:
        print('🔴Please set your API key in the .env file')
        return
    
    openai.api_key = api
    global client
    client = openai.OpenAI()
    
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
    