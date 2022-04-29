from core.stm.actions.AbstractAction import AbstractAction


class DeleteAttributeAction(AbstractAction):

    def __init__(self, entity, attribute) -> None:
        
        self.__entity = entity
        self.__attribute = attribute

    def entity(self):
        return self.__entity

    def attribute(self):
        return self.__attribute

    def info(self):
        return AbstractAction.info(self) + " \n\t delete attribute " + self.attribute() + " from " + self.entity().name()

    def transformation_type(self):
        return "attribute"

    def action_type(self):
        return "delete"
