from modules import bland_ai_api_module as bland_ai_api
from modules import env_module 
from modules import csv_module

def main():
    bland = bland_ai_api.bland_api(env_module.get_api_key())
    csv_mod = csv_module.csv_manager()
    
    

if __name__ == "__main__":
    main()