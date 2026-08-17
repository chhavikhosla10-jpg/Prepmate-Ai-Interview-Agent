import os
from dotenv import load_dotenv

load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY", "")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID", "")
IBM_REGION = os.getenv("IBM_REGION", "jp-tok")

IBM_TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"
IBM_MODEL_ID = os.getenv("IBM_MODEL_ID", "ibm/granite-13b-instruct-v2")

def get_watsonx_generation_url() -> str:
    return f"https://{IBM_REGION}.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-31"
