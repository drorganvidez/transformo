from core.stm.actions.AbstractAction import AbstractAction


class RenameEntityAction(AbstractAction):

    def __init__(self, entity, rename) -> None:
        
        self.__entity = entity
        self.__rename = rename

    def entity(self):
        return self.__entity

    def rename(self):
        return self.__rename

    def info(self):
        return AbstractAction.info(self) + " \n\t old entity:  " + self.__entity.id() + ", new entity: " + self.__rename

    def transformation_type(self):
        return "entity"

    def action_type(self):
        return "rename"