import mysql.connector
from mysql.connector import Error
from modules.env_module import get_sql_host, get_sql_database, get_sql_password, get_sql_user

class MySQLManager:
    def __init__(self):
        self.config = {
            'host': get_sql_host(),
            'user': get_sql_user(),
            'password': get_sql_password(),
            'database': get_sql_database()
        }

        self.connection = None

    # region database creations

    def __get_tables_made(self):
        return self.__fetch_query("SHOW TABLES;")

    def define_required_tables(self):
        current_tbls = self.__get_tables_made()

        if current_tbls:
            order = False
            menu = False
            customer = False
            customer_order = False 
            user = False
            logs = False

            for tbl in current_tbls:                       
                if tbl['Tables_in_ai_takeaway'].lower() == "customer_tbl":
                    customer = True
                if tbl['Tables_in_ai_takeaway'].lower() == "menu_item_tbl":
                    menu = True
                if tbl['Tables_in_ai_takeaway'].lower() == "order_tbl":
                    order = True
                if tbl['Tables_in_ai_takeaway'].lower() == "customer_order_lnk":
                    customer_order = True
                if tbl['Tables_in_ai_takeaway'].lower() == "user_tbl":
                    user = True
                if tbl['Tables_in_ai_takeaway'].lower() == "logs_tbl":
                    logs = True
            
            if not customer:
                self.__define_customer_tbl()
            if not logs:
                self.__define_logs()
            if not user:
                self.__define_user_tbl()
            if not customer_order:
                self.__define_lnk_order_customer()
            if not order:
                self.__define_order_tbl()
            if not menu:
                self.__define_menu_items_tbl()
        else:
            self.__define_customer_tbl()
            self.__define_menu_items_tbl()
            self.__define_order_tbl()
            self.__define_lnk_order_customer()
            self.__define_user_tbl()
            self.__define_logs()

    def __define_customer_tbl(self):
        query = """CREATE TABLE customer_tbl (
        customer_id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
        customer_name VARCHAR(50),
        address VARCHAR(50),
        phone_num VARCHAR(50)
        )"""

        self.__execute_query(query)

    def __define_order_tbl(self):
        query = """CREATE TABLE order_tbl (
        order_id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
        items VARCHAR(50),
        date DATE 
        )"""

        self.__execute_query(query)

    def __define_menu_items_tbl(self):
        query = """CREATE TABLE menu_item_tbl (
        itemid INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
        item_name VARCHAR(50),
        price VARCHAR(50)
        )""" 

        self.__execute_query(query)

    def __define_lnk_order_customer(self):
        query = """CREATE TABLE customer_order_lnk (
        customer_id INT,
        order_id INT,
        PRIMARY KEY(customer_id, order_id),
        FOREIGN KEY (customer_id) REFERENCES customer_tbl(customer_id) ON DELETE CASCADE,
        FOREIGN KEY (order_id) REFERENCES order_tbl(order_id) ON DELETE CASCADE
        )"""

        self.__execute_query(query)

    def __define_user_tbl(self):
        query = """CREATE TABLE user_tbl (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(50),
        password_hash VARCHAR(50),
        role ENUM('user', 'admin') DEFAULT 'user',
        is_active BOOLEAN DEFAULT TRUE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""

        self.__fetch_query(query)

    def __define_logs(self):
        query = """CREATE TABLE logs_tbl (
        log_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        action VARCHAR(255) NOT NULL,
        details TEXT,
        ip_address VARCHAR(45),
        user_agent VARCHAR(255),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user_tbl(user_id) ON DELETE SET NULL
        );"""

        self.__execute_query(query)

    # endregion

    def drop_all_tbls(self):
        current_tables = self.__get_tables_made()

        for tbls in current_tables:
                query = f"DROP TABLE {tbls['Tables_in_ai_takeaway']}"
                self.__execute_query(query)

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

    def __execute_query(self, query, params=None):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("✅ Query executed successfully")
        except Error as e:
            self.connection.rollback()
            print(f"❌ Error executing query: {e}")
        finally:
            if cursor:
                cursor.close()

    def __fetch_query(self, query, params=None):
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
