class CreateAttributeAction:

    def __init__(self, entity, attribute, type) -> None:
        
        self.__entity = entity
        self.__attribute = attribute
        self.__type = type

    def entity(self):
        return self.__entity

    def attribute(self):
        return self.__attribute

    def type(self):
        return self.__type