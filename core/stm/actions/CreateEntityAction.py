from core.stm.actions.AbstractAction import AbstractAction


class CreateEntityAction(AbstractAction) :

    def __init__(self, entity) -> None:
        
        self._entity = entity

    def entity(self):
        return self._entity

    def info(self):
        return AbstractAction.info(self) + " \n\t new entity:  " + self._entity.id()
