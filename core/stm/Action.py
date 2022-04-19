

from typing import Any
from core.stm.actions.DeleteAttributeAction import DeleteAttributeAction
from core.stm.actions.RenameAttributeAction import RenameAttributeAction
from core.stm.actions.RetypeAttributeAction import RetypeAttributeAction


class Action:

    def __init__(self, sdm, item, transformation_action) -> None:
        
        self.__sdm = sdm
        self.__item = item
        self.__transformation_action = transformation_action
        self.__type = item.getAttribute('type')

        self.__apply : Any = None
        self.__explore()

    def __explore(self):

        if self.__transformation_action == "entity":
            pass

        if self.__transformation_action == "attribute":

            if self.__type == "retype":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
                retype = self.__item.getElementsByTagName("retype")[0].childNodes[0].data

                # create action
                self.__apply = RetypeAttributeAction(entity = entity, attribute = attribute, retype = retype)

            if self.__type == "rename":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
                rename = self.__item.getElementsByTagName("rename")[0].childNodes[0].data

                # create action
                self.__apply = RenameAttributeAction(entity = entity, attribute = attribute, rename = rename)

            if self.__type == "delete":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data

                # create action
                self.__apply = DeleteAttributeAction(entity = entity, attribute = attribute)
           

        if self.__transformation_action == "relation":
            pass


    def apply(self):
        return self.__apply  

    def type(self):
        return self.__type

    def __str__(self) -> str:
        
        string = "Type = {type}".format(type = self.__type)

        return string