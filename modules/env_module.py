from dotenv import load_dotenv
import os

def get_api_key() -> str:
    load_dotenv()

    return os.environ['api_key']