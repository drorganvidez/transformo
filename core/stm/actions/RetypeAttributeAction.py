class RetypeAttributeAction:

    def __init__(self, entity, attribute, retype) -> None:
        
        self.__entity = entity
        self.__attribute = attribute
        self.__retype = retype

    def entity(self):
        return self.__entity

    def attribute(self):
        return self.__attribute

    def retype(self):
        return self.__retype