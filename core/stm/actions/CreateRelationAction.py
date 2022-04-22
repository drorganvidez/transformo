class CreateRelationAction:

    def __init__(self, first_entity, second_entity) -> None:
        
        self.__first_entity = first_entity
        self.__second_entity = second_entity

    def first_entity(self):
        return self.__first_entity

    def second_entity(self):
        return self.__second_entity