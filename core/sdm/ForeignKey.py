from xml.dom.minidom import Entity


class ForeignKey:

    def __init__(self, references_entity) -> None:
        self.__references_entity : Entity = references_entity
        pass

    def references_entity(self) -> Entity:  
        return self.__references_entity

    def __str__(self) -> str:

        string = "Foreign key references to '{references_entity}'\n".format( references_entity = self.__references_entity)

        return string