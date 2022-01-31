import os
from dotenv import load_dotenv
import mysql.connector
import re
from mysql.connector import FieldType

from core.mysql.Table import Table

class MySQLExtractor:

    def __init__(self, env) -> None:

        load_dotenv()

        if(len(env) != 4):
            raise ValueError("Error, the number of environment variables is not correct")

        self.__host = os.getenv(env[0])
        self.__database = os.getenv(env[1])
        self.__user = os.getenv(env[2])
        self.__password = os.getenv(env[3])

        self.__tables = []

        mydb = self.connect()
        mydb.close()

    def connect(self):
        return mysql.connector.connect(host=self.__host,database=self.__database,user=self.__user,password=self.__password)

    def extract(self):
        self.extract_tables_names()
        self.extract_columns()

    def extract_tables_names(self):

        mydb = self.connect()
    
        cursor = mydb.cursor()
 
        cursor.execute("SHOW TABLES")

        for (table_name,) in cursor:
            table = Table(table_name = table_name)
            self.__tables.append(table)

        mydb.close()

    def extract_columns(self):

        mydb = self.connect()
    
        cursor = mydb.cursor()

        for table in self.__tables:

            cursor.execute("DESCRIBE " + table.name())

            bulk_column_data = cursor.fetchall()

            table.set_columns(bulk_column_data)

        mydb.close()

    def tables(self):
        return self.__tables