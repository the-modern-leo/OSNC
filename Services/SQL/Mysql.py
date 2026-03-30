# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import mysql
from lxml.html import document_fromstring
from mysql.connector import errorcode,connect,Error
from auth import mysql

DBName = 'NetworkDB'

TABLES = {}
TABLES['networkdevice'] = (
    "CREATE TABLE networkdevice ("
    "  NetID int NOT NULL AUTO_INCREMENT,"
    "  ipaddress VARCHAR(16) NOT NULL,"
    "  hostname VARCHAR(255) NOT NULL,"
    "  dnsname VARCHAR(255) default NULL,"
    "  devicetype VARCHAR(255) default NULL,"
    "  Switchport VARCHAR(255) default NULL,"
    
    "  PRIMARY KEY (NetID)"
    
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;")

TABLES['Endpoints'] = (
    "CREATE TABLE Endpoints ("
    "  endpointsID int NOT NULL,"
    "  ipaddress VARCHAR(16) NULL,"
    "  dnsname VARCHAR(255) default NULL,"
    "  switchports VARCHAR(255) default NULL,"
    "  macaddress VARCHAR(255) NOT NULL,"
    "  networkdevice_NetID INT NOT NULL,"
    "  INDEX net_ID (networkdevice_NetID),"
    
    "  FOREIGN KEY (networkdevice_NetID)"
    "  REFERENCES networkdevice(NetID)"
    "  ON DELETE CASCADE"
    
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;")

TABLES['CRCErrors'] = (
    "CREATE TABLE CRCErrors ("
    "  crcID int NOT NULL AUTO_INCREMENT,"
    "  networkdeviceID INT NOT NULL,"
    "  switchport VARCHAR(255) NOT NULL,"
    "  FirstCRC BIGINT NOT NULL,"
    "  CompareCRC BIGINT NOT NULL,"

    "  PRIMARY KEY (crcID),"
    "  FOREIGN KEY (networkdeviceID)"
    "  REFERENCES networkdevice(NetID)"
    "  ON DELETE CASCADE"

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
        """
        Creates a new database with the specified name if it does not already exist
        and sets it as the active database.

        If the database does not exist, the method tries to create it. If creation
        fails, the process terminates with an error message. If the database exists
        and is successfully set as the active database, operations will use it.

        Args:
            DBName (str): Name of the database to be created or activated.

        Raises:
            mysql.connector.Error: If any error occurs during the database creation or
                activation, detailed messages will be printed, and in some cases, the
                process will terminate.
        """
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

    def create_tables(self):
        """
        Creates tables in the database using predefined table descriptions.

        This method ensures that tables described within the "TABLES" dictionary are
        created in the specified database. For each table, it attempts to execute
        the corresponding SQL command and provides feedback on whether the table
        was successfully created, already exists, or if an error occurred.

        Raises:
            mysql.connector.Error: If any SQL execution error occurs, except for
                when the table already exists.

        """
        self.cursor.execute(f"USE {DBName}")
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print(f"Creating table {table_name}: ", end='')
                self.cursor.execute(table_description)
            except Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def delete_tables(self,tablename):
        """
        Deletes a specified table from the database.

        This method checks if the specified table exists in the predefined list of
        tables (`TABLES`), and if it exists, executes a SQL command to drop the table
        from the database. If the table does not exist in the database, an error is
        raised, which is handled to provide appropriate feedback.

        Args:
            tablename: Name of the table to be deleted.

        Raises:
            Error: If there is an issue executing the SQL command to delete the table.
        """
        self.cursor.execute(f"USE {DBName}")
        for table_name in TABLES:
            if tablename == table_name:
                table_description = f"DROP TABLE {table_name}"
                try:
                    print(f"Deleting table {table_name}: ", end='')
                    self.cursor.execute(table_description)
                except Error as err:
                    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print("already exists.")
                    else:
                        print(err.msg)
                else:
                    print("OK")

    def _insert_record(self,SQL,val):
        """
        Executes an SQL INSERT operation to add a record to the specified table.

        This method accepts a provided SQL table name and a tuple of values, and
        inserts a new record into the specified table using those values. If the
        operation encounters an error, it logs the error message. Upon successful
        insertion, the transaction is committed, and a success message is printed.

        Args:
            SQL (str): The name of the table where the record will be inserted.
            val (tuple): A tuple containing the values for the new record.

        """
        self.cursor.execute(f"USE {DBName}")
        try:
            print(SQL)
            self.cursor.execute(f"INSERT INTO {SQL}",val)
            self.cnx.commit()
        except Error as err:
                print(err.msg)
        else:
            print(f"record inserted.")

    def _delete_record(self,SQL):
        self.cursor.execute(f"USE {DBName}")
        try:
            print(SQL)
            self.cursor.execute(f"DELETE FROM {SQL}")
            self.cnx.commit()
        except Error as err:
                print(err.msg)
        else:
            print(f"record deleted.")

    def _update_record(self,SQL):
        self.cursor.execute(f"USE {DBName}")
        try:
            print(SQL)
            self.cursor.execute(f"UPDATE {SQL}")
            self.cnx.commit()
        except Error as err:
                print(err.msg)
        else:
            print(f"record updated.")

    def _select_record(self,SQL):
        self.cursor.execute(f"USE {DBName}")
        try:
            print(SQL)
            self.cursor.execute(f"SELECT {SQL}")
            myresult = self.cursor.fetchall()
        except Error as err:
                print(err.msg)
        else:
            return myresult