class Key:

    def __init__(self, key_data) -> None:

        self.__key_data = key_data

        self.__table_name = key_data[0]
        self.__non_unique = key_data[1]
        self.__key_name = key_data[2]
        self.__seq_in_index = key_data[3]
        self.__column_name = key_data[4]
        self.__collation = key_data[5]
        self.__cardinality = key_data[6]
        self.__sub_part = key_data[7]
        self.__packed = key_data[8]
        self.__null = key_data[9]
        self.__index_type = key_data[10]
        self.__comment = key_data[11]
        self.__index_comment = key_data[12]
        self.__visible = key_data[13]
        self.__expression = key_data[14]

    def is_primary(self):
        return self.__key_name == 'PRIMARY'

    def __str__(self) -> str:
        return str(self.__key_data)