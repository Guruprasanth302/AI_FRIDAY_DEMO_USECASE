# ai_integration.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve SerpApi key and OpenRouter's model details from environment variables
serpapi_key = os.getenv('SERPAPI_API_KEY')
openrouter_model_endpoint = os.getenv('OPENROUTER_MODEL_ENDPOINT')
openrouter_model_name = os.getenv('OPENROUTER_MODEL_NAME')

# Function to get code analysis and suggestions using OpenRouter's model (like GPT-3.5)
def get_ai_suggestions(code, checklist):
    """
    Uses OpenRouter's model endpoint to analyze the code and generate suggestions based on the provided checklist.
    
    Args:
    - code (str): The code to be analyzed.
    - checklist (str): A list of code quality checks to be followed (e.g., readability, naming conventions, etc.).
    
    Returns:
    - str: Structured output with observations and suggestions.
    """
    
    prompt = f"""
    You are an AI that checks the quality of code. The following code should be analyzed against a checklist.
    
    Code:
    {code}
    
    Checklist:
    {checklist}
    
    Observations and Suggestions:
    """

    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "model": openrouter_model_name,  # Use the model name from the environment variable
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
    }

    try:
        response = requests.post(openrouter_model_endpoint, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        suggestions = result.get('choices', [])[0].get('text', '').strip()
        
        return suggestions
    
    except requests.exceptions.RequestException as e:
        print(f"Error during OpenRouter API call: {e}")
        return "Unable to fetch AI suggestions at the moment."


# Optional: Use SerpApi for search functionality if needed in the app

def search_with_serpapi(query):
    """
    Uses SerpApi to perform a search query and get results from a search engine like Google.
    
    Args:
    - query (str): The search query.
    
    Returns:
    - dict: Search results from SerpApi.
    """
    url = f"https://serpapi.com/search?q={query}&api_key={serpapi_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during SerpApi search: {e}")
        return {"error": "Unable to fetch search results."}