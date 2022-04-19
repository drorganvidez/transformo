class RenameAttributeAction:

    def __init__(self, entity, attribute, rename) -> None:
        
        self.__entity = entity
        self.__attribute = attribute
        self.__rename = rename

    def entity(self):
        return self.__entity

    def attribute(self):
        return self.__attribute

    def rename(self):
        return self.__rename