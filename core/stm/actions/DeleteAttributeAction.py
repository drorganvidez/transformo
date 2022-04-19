class DeleteAttributeAction:

    def __init__(self, entity, attribute) -> None:
        
        self.__entity = entity
        self.__attribute = attribute

    def entity(self):
        return self.__entity

    def attribute(self):
        return self.__attribute