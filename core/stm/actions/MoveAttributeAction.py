class MoveAttributeAction:

    def __init__(self, entity_from, entity_to, attribute, type) -> None:
        
        self.__entity_from = entity_from
        self.__entity_to = entity_to
        self.__attribute = attribute
        self.__type = type

    def entity_from(self):
        return self.__entity_from

    def entity_to(self):
        return self.__entity_to

    def attribute(self):
        return self.__attribute

    def type(self):
        return self.__type