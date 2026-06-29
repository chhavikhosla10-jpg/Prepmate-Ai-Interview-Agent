def clean_text(text: str) -> str:
    return " ".join(text.strip().split())

def is_ibm_config_available(api_key: str, project_id: str) -> bool:
    return bool(api_key and project_id)
