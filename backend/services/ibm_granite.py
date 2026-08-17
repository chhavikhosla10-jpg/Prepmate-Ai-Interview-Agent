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
            "apikey": IBM_API_KEY.strip(),
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        timeout=30,
    )
    if not response.ok:
        raise RuntimeError(
            f"IAM token request failed ({response.status_code}): {response.text}"
        )
    return response.json()["access_token"]


def generate_with_granite(prompt: str) -> str:
    if not IBM_API_KEY or not IBM_PROJECT_ID:
        raise ValueError(
            "IBM credentials missing. Add IBM_API_KEY and IBM_PROJECT_ID in backend/.env"
        )

    token = get_access_token()

    payload = {
        "model_id": IBM_MODEL_ID.strip(),
        "project_id": IBM_PROJECT_ID.strip(),
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 1800,
            "min_new_tokens": 100,
            "temperature": 0.7,
            "repetition_penalty": 1.1
        }
    }

    url = get_watsonx_generation_url()

    response = requests.post(
        url,
        json=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        timeout=60
    )

    # THIS is the important change: surface IBM's actual JSON error body
    # instead of letting raise_for_status() swallow it into a generic message.
    if not response.ok:
        raise RuntimeError(
            f"watsonx.ai request failed ({response.status_code}) "
            f"for url={url} model_id={payload['model_id']} "
            f"project_id={payload['project_id'][:8]}...\n"
            f"Response body: {response.text}"
        )

    data = response.json()
    return data["results"][0]["generated_text"]