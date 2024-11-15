# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import mysql
from mysql.connector import errorcode,connect,Error
from auth import mysql

DBName = 'NetworkDB'

TABLES = {}
TABLES['networkdevice'] = (
    "CREATE TABLE networkdevice ("
    "  NetID int NOT NULL AUTO_INCREMENT,"
    "  ipaddress VARCHAR(16) NOT NULL UNIQUE,"
    "  hostname VARCHAR(255) NOT NULL,"
    "  dnsname VARCHAR(255) default NULL,"
    "  devicetype VARCHAR(255) default NULL,"
    "  deafultgateway VARCHAR(100) default NULL,"
    
    "  PRIMARY KEY (NetID)"
    
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;")

TABLES['Endpoints'] = (
    "CREATE TABLE Endpoints ("
    "  endpointsID int NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "  ipaddress VARCHAR(16) NULL,"
    "  dnsname VARCHAR(255) default NULL,"
    "  switchport VARCHAR(255) default NULL,"
    "  macaddress VARCHAR(255) NOT NULL UNIQUE,"
    "  company VARCHAR(255) default NULL,"
    "  NetID INT NOT NULL,"
    
    "  FOREIGN KEY (NetID)"
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
        self.cursor.execute(f"USE {DBName}")
        try:
            print(SQL)
            self.cursor.execute(f"INSERT INTO {SQL}",val)
            self.cnx.commit()
        except Error as err:
                print(err.msg)
                if "duplicate entry" in str(err.msg).lower():
                    return err.msg
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

    def GetallSwitches(self):
        return self._select_record("* FROM networkdevice WHERE devicetype = 'Switch'")
    def addendpoint(self,sql,tuplevalue):
        return self._insert_record(sql,tuplevalue)

    def Getallendpoints(self):
        return self._select_record(f"* FROM endpoints")
    def GetAccessLayerSwitchsWithNoEndpoints(self):
        switchestoCollectEndpoints = set()
        switcheswithendpoints = set()
        allswitches = set()
        results = self.GetallSwitches()
        endpoints = self.Getallendpoints()
        for endpoint in endpoints:
            switcheswithendpoints.add(endpoint[5])
        for sw in results:
            allswitches.add(sw[0])
        switch_ids_with_no_endpoints = allswitches - switcheswithendpoints
        switch_tuples_with_no_endpoints = set()
        for swTuple in results:
            if swTuple[0] in switch_ids_with_no_endpoints:
                switch_tuples_with_no_endpoints.add(swTuple)
        for switch in results:
            for endpoint in endpoints:
                if not endpoint[5] == switch[0]:
                    switchestoCollectEndpoints.add(switch)
                    continue
        return list(switch_tuples_with_no_endpoints)
