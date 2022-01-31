class Column:

    def __init__(self, column_data) -> None:

        self.__column_data = column_data

        self.__field = self.__column_data[0]
        self.__type = self.__column_data[1]
        self.__null = self.__column_data[2]
        self.__key = self.__column_data[3]
        self.__default = self.__column_data[4]
        self.__extra = self.__column_data[5]

    def field(self) -> str:
        return self.__field

    def type(self):
        return self.__type

    def is_null(self):
        return self.__null == 'YES'

    def key(self):
        return self.__key

    def default(self):
        return self.__default

    def extra(self):
        return self.__extra

    def __str__(self) -> str:
        return str(self.__column_data)