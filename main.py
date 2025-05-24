from modules import bland_ai_api_module as bland_ai_api
# from modules import env_module
from modules import csv_module
from modules import mysql_module

def main():
    # bland = bland_ai_api.bland_api(env_module.get_api_key())
    csv_mod = csv_module.csv_manager()
    database = mysql_module.MySQLManager()

    database.connect()
    database.define_required_tables()
    # database.drop_all_tbls()

    database.disconnect()
    
    

if __name__ == "__main__":
    main()