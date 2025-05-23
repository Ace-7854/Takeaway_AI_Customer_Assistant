from dotenv import load_dotenv
import os

def get_api_key() -> str:
    load_dotenv()

    return os.environ['api_key']

def get_pathway_id() -> str:
    load_dotenv()

    return os.environ['pathway_id']

def get_sql_host():
    load_dotenv()

    return os.environ['sql_host']

def get_sql_user():
    load_dotenv()

    return os.environ['sql_user']

def get_sql_password():
    load_dotenv()

    return os.environ['sql_password']

def get_sql_database():
    load_dotenv()

    return os.environ['sql_database']


# sql_host=94.0.81.28
# sql_user=edi
# sql_password=Tzg4H$uzk$2co8rNS^hJ
# sql_database=ai_takeaway