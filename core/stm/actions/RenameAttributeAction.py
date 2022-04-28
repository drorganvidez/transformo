from core.stm.actions.AbstractAction import AbstractAction


class RenameAttributeAction(AbstractAction):

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

    def info(self):
        return AbstractAction.info(self) + " \n\t rename attribute " + self.attribute() + " to " + self.rename() + " in " + self.entity().name()

    def transformation_type(self):
        return "attribute"

    def action_type(self):
        return "rename"