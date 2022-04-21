from typing import Any
from core.stm.actions.CreateAttributeAction import CreateAttributeAction
from core.stm.actions.CreateEntityAction import CreateEntityAction
from core.stm.actions.DeleteAttributeAction import DeleteAttributeAction
from core.stm.actions.MoveAttributeAction import MoveAttributeAction
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
            
            if self.__type == "create":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data

                # update entity
                self.__sdm.add_entity(element)

                entity = self.__sdm.get_entity_by_id(element)

                # create action
                self.__apply = CreateEntityAction(entity = entity)

        if self.__transformation_action == "attribute":

            if self.__type == "create":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute_name = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
                type = self.__item.getElementsByTagName("type")[0].childNodes[0].data

                # update attibute
                self.__sdm.add_attribute(entity = entity, attribute_name = attribute_name, attribute_type = type)

                # create action
                self.__apply = CreateAttributeAction(entity = entity, attribute = attribute_name, type = type)


            if self.__type == "retype":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
                retype = self.__item.getElementsByTagName("retype")[0].childNodes[0].data

                # update attribute
                self.__sdm.edit_attribute_type(entity = entity, attribute_name = attribute, retype = retype)

                # create action
                self.__apply = RetypeAttributeAction(entity = entity, attribute = attribute, retype = retype)

            if self.__type == "move":

                # basic data
                element_from = self.__item.getElementsByTagName("from")[0].childNodes[0].data
                element_to = self.__item.getElementsByTagName("to")[0].childNodes[0].data
                entity_from = self.__sdm.get_entity_by_id(element_from)
                entity_to = self.__sdm.get_entity_by_id(element_to)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
                type = self.__item.getElementsByTagName("type")[0].childNodes[0].data

                # update attribute
                self.__sdm.add_attribute(entity = entity_to, attribute_name = attribute, attribute_type = type)
                self.__sdm.delete_attribute(entity = entity_from, attribute_name = attribute)

                # create action
                self.__apply = MoveAttributeAction(entity_from = entity_from, entity_to = entity_to, attribute = attribute, type = type)


            if self.__type == "rename":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
                rename = self.__item.getElementsByTagName("rename")[0].childNodes[0].data

                # update attribute
                self.__sdm.edit_attribute_name(entity = entity, attribute_name = attribute, rename = rename)

                # create action
                self.__apply = RenameAttributeAction(entity = entity, attribute = attribute, rename = rename)

            if self.__type == "delete":

                # basic data
                element = self.__item.getElementsByTagName("entity")[0].childNodes[0].data
                entity = self.__sdm.get_entity_by_id(element)
                attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data

                # update attribute
                self.__sdm.delete_attribute(entity = entity, attribute_name = attribute)

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