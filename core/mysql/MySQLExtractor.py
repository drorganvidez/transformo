import os
from dotenv import load_dotenv
import mysql.connector
import re

class MySQLExtractor:

    def __init__(self, env) -> None:

        load_dotenv()

        if(len(env) != 4):
            raise ValueError("Error, the number of environment variables is not correct")

        self.__host = os.getenv(env[0])
        self.__database = os.getenv(env[1])
        self.__user = os.getenv(env[2])
        self.__password = os.getenv(env[3])

        self.__tables_names = []

        mydb = self.connect()
        mydb.close()

    def connect(self):
        return mysql.connector.connect(host=self.__host,database=self.__database,user=self.__user,password=self.__password)

    def extract(self):
        self.extract_tables_names()
        

    def extract_tables_names(self):

        mydb = self.connect()
    
        cursor = mydb.cursor()
 
        cursor.execute("SHOW TABLES")

        for (table_name,) in cursor:
            self.__tables_names.append(table_name)
            print(table_name)

        mydb.close()
