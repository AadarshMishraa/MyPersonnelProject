from dotenv import load_dotenv
import os
import openai
import time
from openai.error import RateLimitError

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in .env file.")
    exit(1)

openai.api_key = api_key

# Global cache dictionary to store generated scripts by prompt
script_cache = {}

def call_openai_api(prompt):
    """Helper function to call the OpenAI API."""
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful script-writing assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )

def generate_script(prompt):
    """Generate a script based on the user's prompt, with caching and error handling."""
    
    # Return from cache if available
    if prompt in script_cache:
        return script_cache[prompt]

    try:
        response = call_openai_api(prompt)
        script = response['choices'][0]['message']['content'].strip()
        script_cache[prompt] = script
        return script

    except RateLimitError:
        print("⚠️ Rate limit exceeded. Retrying after 60 seconds...")
        time.sleep(60)  # Backoff time
        try:
            response = call_openai_api(prompt)
            script = response['choices'][0]['message']['content'].strip()
            script_cache[prompt] = script
            return script
        except RateLimitError:
            return "❌ API quota exceeded. Please check your billing details or try again later."

    except Exception as e:
        print("❌ An error occurred:", e)
        return "An unexpected error occurred while generating the script."

