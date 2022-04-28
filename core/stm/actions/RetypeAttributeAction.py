from core.stm.actions.AbstractAction import AbstractAction


class RetypeAttributeAction(AbstractAction):

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

    def info(self):
        return AbstractAction.info(self) + " \n\t retype attribute " + self.attribute() + " to " + self.retype() + " in " + self.entity().name()

    def transformation_type(self):
        return "attribute"

    def action_type(self):
        return "retype"