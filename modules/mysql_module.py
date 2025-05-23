import mysql.connector
from mysql.connector import Error
from env_module import get_sql_host, get_sql_database, get_sql_password, get_sql_user

class MySQLManager:
    def __init__(self):
        self.config = {
            'host': get_sql_host(),
            'user': get_sql_user(),
            'password': get_sql_password(),
            'database': get_sql_database()
        }
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                print("✅ Connected to MySQL database")
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("🔌 MySQL connection closed")

    def execute_query(self, query, params=None):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("✅ Query executed successfully")
        except Error as e:
            print(f"❌ Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()

    def fetch_query(self, query, params=None):
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"❌ Error fetching data: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
