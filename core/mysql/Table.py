from core.mysql.Column import Column


class Table:

    def __init__(self, table_name) -> None:

        self.__table_name = table_name
        self.__columns = []

    def name(self) -> str:
        return self.__table_name

    def set_columns(self, bulk_column_data):
        
        for column_data in bulk_column_data:
            column = Column(column_data)
            self.__columns.append(column)

    def columns(self):
        return self.__columns

    def __str__(self) -> str:
        string = "Table `" + self.name() + "`"

        string = string + "\n\tColumns: " + str(len(self.columns()))

        for columns in self.columns():
            string = string + "\n\t" + str(columns)

        return "\n" + string
