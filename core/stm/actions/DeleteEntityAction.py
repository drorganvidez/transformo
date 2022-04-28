from core.stm.actions.AbstractAction import AbstractAction


class DeleteEntityAction(AbstractAction):

    def __init__(self, entity) -> None:
        
        self._entity = entity

    def entity(self):
        return self._entity

    def info(self):
        return AbstractAction.info(self) + " \n\t delete entity:  " + self._entity.id()

    def transformation_type(self):
        return "entity"

    def action_type(self):
        return "delete"