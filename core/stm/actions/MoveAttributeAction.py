from core.stm.actions.AbstractAction import AbstractAction


class MoveAttributeAction(AbstractAction):

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

    def info(self):
        return AbstractAction.info(self) + " \n\t move attribute " + self.attribute() + " : " + self.type() + ", from " + self.entity_from().name() + " to " + self.entity_to().name()

    def transformation_type(self):
        return "attribute"

    def action_type(self):
        return "move"
