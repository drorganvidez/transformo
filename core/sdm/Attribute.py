class Attribute:

    def __init__(self, attribute_item = None, static = False, attribute_name = None, attribute_type = None):

        if not static:

            self.attribute_item = attribute_item

            self.__name = self.attribute_item.getElementsByTagName("name")[0].childNodes[0].data
            self.__type = self.attribute_item.getElementsByTagName("type")[0].childNodes[0].data

        else:

            self.__name = attribute_name
            self.__type = attribute_type

    def __eq__(self, __o: object) -> bool:
        pass

    def name(self) -> str:
        return self.__name

    def type(self) -> str:
        return self.__type

    def set_name(self, name) -> None:
        self.__name = name

    def set_type(self, type) -> None:
        self.__type = type

    def __str__(self) -> str:
        return "Attribute: (" + self.__type + ") " + self.__name