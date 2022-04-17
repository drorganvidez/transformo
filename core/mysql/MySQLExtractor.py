import os
from dotenv import load_dotenv
import mysql.connector
import re
from mysql.connector import FieldType

from core.mysql.Table import Table

class MySQLExtractor:

    def __init__(self) -> None:

        load_dotenv()
        
        self.__host =  os.getenv('DB_HOST')
        self.__database = os.getenv('DB_DATABASE')
        self.__user = os.getenv('DB_USER')
        self.__password = os.getenv('DB_PASSWORD')
        self.__port = int(os.getenv('DB_PORT'))

        self.__tables = []

        mydb = self.connect()
        mydb.close()

    

    def connect(self):
        return mysql.connector.connect(
            host=self.__host,
            database=self.__database,
            user=self.__user,
            password=self.__password,
            port=int(self.__port))

    def extract(self):

        self.extract_tables_names()
        self.extract_columns()
        self.extract_keys()

    def generate_simple_database_model(self, output = ""):

        filename = None
        f = None

        if(output == ""):
            filename = "sdm/proof.txt"
        else:
            filename = "sdm/"+output

        try:
            f = open(filename, "x")
        except:
            f = open(filename, "w").close()
            f = open(filename, "w")

        data_stream = ""

        # start XML
        data_stream = self.__get_data_stream(stub_name = "core/sdm/stubs/start_xml.stub")
        self.__write_in_file(data_stream=data_stream, file = f)

        for table in self.tables():
            # start entity
            data_stream = self.__get_data_stream(stub_name = "core/sdm/stubs/start_entity.stub")
            self.__replace(data_stream, "{entity_id}", table.name())
            self.__replace(data_stream, "{entity_name}", table.name())
            self.__write_in_file(data_stream=data_stream, file = f)

            for column in table.columns():
                # start attribute
                data_stream = self.__get_data_stream(stub_name = "core/sdm/stubs/start_attribute.stub")
                self.__replace(data_stream, "{attribute_name}", str(column.field()))
                self.__replace(data_stream, "{attribute_type}", str(column.type()))
                self.__write_in_file(data_stream=data_stream, file = f)
                
                #end attribute
                data_stream = self.__get_data_stream(stub_name = "core/sdm/stubs/end_attribute.stub")
                self.__write_in_file(data_stream=data_stream, file = f)

            # end entity
            data_stream = self.__get_data_stream(stub_name = "core/sdm/stubs/end_entity.stub")
            self.__write_in_file(data_stream=data_stream, file = f)

        # TODO: Extract relationships between entities


        # end XML
        data_stream = self.__get_data_stream(stub_name = "core/sdm/stubs/end_xml.stub")
        self.__write_in_file(data_stream=data_stream, file = f)
        
    def __replace(self, data_stream, before, after):

        for i in range(len(data_stream)):
            data_stream[i] = data_stream[i].replace(before, after)

    def __get_data_stream(self, stub_name):
        data_stream = ""
        with open (stub_name, "r") as myfile:
            data_stream = myfile.readlines()
        return data_stream

    def __write_in_file(self, data_stream, file):
        for data in data_stream:
            file.write(data)

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

    def extract_keys(self):
        mydb = self.connect()
    
        cursor = mydb.cursor()

        for table in self.__tables:

            cursor.execute("SHOW KEYS FROM "+ table.name() +"")

            bulk_key_data = cursor.fetchall()

            table.set_keys(bulk_key_data)

        print("FOREIGN KEYS")
        cursor.execute("SELECT * FROM information_schema.table_constraints WHERE table_name='postmeta';")
        print(cursor.fetchall())

        mydb.close()

    def get_table(self, table_name):

        res = None

        for table in self.tables():
            if(table.name() == table_name):
                res = table
                break

        return res

    def tables(self):
        return self.__tables
        