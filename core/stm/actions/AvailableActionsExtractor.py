from numpy import void
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.AvailableAction import AvailableAction
from core.stm.actions.CreateEntityAction import CreateEntityAction
from core.stm.actions.DeleteEntityAction import DeleteEntityAction
from core.stm.actions.RenameEntityAction import RenameEntityAction


class AvailableActionsExtractor:

    def __init__(self, sdm_source : SimpleDatabaseModel, sdm_target: SimpleDatabaseModel) -> None:

        self._A = sdm_source
        self._B = sdm_target
        self._available_actions : list[AvailableAction] = list()

        self.extract_create_entity_actions()
        self.extract_rename_entity_actions()
        self.extract_delete_entity_actions()

    def available_actions(self):
        return self._available_actions

    def add_action(self, action : any) -> void:

        available_action = AvailableAction(action)
        self._available_actions.append(available_action)

    # extractions

    def extract_create_entity_actions(self):

        for e in self._B.entities():
            if not self._A.contains_entity_by_id(e):

                action = CreateEntityAction(e)
                self.add_action(action)


    def extract_rename_entity_actions(self):

        for eB in self._B.entities():

            for eA in self._A.entities():

                if(eA.contains_same_attributes(eB)):

                    action = RenameEntityAction(entity = eA, rename = eB.id())
                    self.add_action(action)

    def extract_delete_entity_actions(self):

        for e in self._A.entities():
            if not self._B.contains_entity_by_id(e):

                action = DeleteEntityAction(e)
                self.add_action(action)



    def print(self):

        print("########################################")
        print("Available actions")
        print("########################################")
        print()

        for a in self._available_actions:

            print("-> " + str(a))
            print()