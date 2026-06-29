import requests
from utils.config import (
    IBM_API_KEY,
    IBM_PROJECT_ID,
    IBM_TOKEN_URL,
    IBM_MODEL_ID,
    get_watsonx_generation_url
)

def get_access_token() -> str:
    response = requests.post(
        IBM_TOKEN_URL,
        data={
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
            "apikey": IBM_API_KEY,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()["access_token"]

def generate_with_granite(prompt: str) -> str:
    if not IBM_API_KEY or not IBM_PROJECT_ID:
        raise ValueError("IBM credentials missing. Add IBM_API_KEY and IBM_PROJECT_ID in backend/.env")

    token = get_access_token()

    payload = {
        "model_id": IBM_MODEL_ID,
        "project_id": IBM_PROJECT_ID,
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 900,
            "min_new_tokens": 100,
            "temperature": 0.7,
            "repetition_penalty": 1.1
        }
    }

    response = requests.post(
        get_watsonx_generation_url(),
        json=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        timeout=60
    )
    response.raise_for_status()
    data = response.json()
    return data["results"][0]["generated_text"]
