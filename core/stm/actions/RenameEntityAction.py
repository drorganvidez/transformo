class RenameEntityAction:

    def __init__(self, entity, rename) -> None:
        
        self.__entity = entity
        self.__rename = rename

    def entity(self):
        return self.__entity

    def rename(self):
        return self.__rename