# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import mysql
from mysql.connector import errorcode,connect
from auth import mysql

DBName = 'NetworkDB'

TABLES = {}
TABLES['Routers'] = (
    "CREATE TABLE Routers ("
    "  routerID int NOT NULL AUTO_INCREMENT,"
    "  ipaddress VARCHAR(16) NOT NULL,"
    "  hostname VARCHAR(255) NOT NULL,"
    "  dnsname VARCHAR(255) default NULL,"
    "  PRIMARY KEY (routerID)"
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;")

class DB(object):
    def __enter__(self):
        try:
            self.cnx = connect(user=mysql.usr, password=mysql.password,
                                          host='127.0.0.1')
            self.cursor = self.cnx.cursor()
            return self

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.cnx.close()
    def create_database(self,DBName):
        try:
            self.cursor.execute(
                f"CREATE DATABASE {DBName} DEFAULT CHARACTER SET 'utf8'")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")
            exit(1)

        try:
            self.cursor.execute(f"USE {DBName}")
        except mysql.connector.Error as err:
            print(f"Database {DBName} does not exists.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(DBName)
                print(f"Database {DBName} created successfully.")
                self.cnx.database = DBName
            else:
                print(err)
                exit(1)
    def create_table(self,DBName):
        self.cursor.execute(f"USE {DBName}")
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print(f"Creating table {table_name}: ", end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def UpdateData(self):
