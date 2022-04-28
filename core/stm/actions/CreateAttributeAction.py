from core.stm.actions.AbstractAction import AbstractAction


class CreateAttributeAction(AbstractAction):

    def __init__(self, entity, attribute, type) -> None:
        
        self._entity = entity
        self._attribute = attribute
        self._type = type

    def entity(self):
        return self._entity

    def attribute(self) -> str:
        return self._attribute

    def type(self):
        return self._type

    def info(self):
        return AbstractAction.info(self) + " \n\t new attribute:  " + self.attribute() + " : " + self.type() + " in entity " + self.entity().name()

    def transformation_type(self):
        return "attribute"

    def action_type(self):
        return "create"
