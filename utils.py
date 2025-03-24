import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def query_llm(prompt):
    """
    Query OpenAI's LLM to generate a response for a given prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.AuthenticationError:
        return "Error: Invalid API key. Please check your .env file."
    except Exception as e:
        return f"Error: {str(e)}"
