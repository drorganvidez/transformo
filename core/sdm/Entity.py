from core.sdm.Attribute import Attribute
from core.sdm.ForeignKey import ForeignKey
from core.sdm.Relation import Relation


class Entity:

    def __init__(self, item = None, static = False, id = None):

        if not static:

            self.item = item

            self.__name = item.getElementsByTagName("name")[0].childNodes[0].data

            self.__id = item.getAttribute('id')

            self.__attributes_items : list[Attribute] = list()

            self.__read_attributes(item.getElementsByTagName("attribute"))

            self.__relations_items : list[Relation] = list()

            self.__foreign_keys : list[ForeignKey] = list()

        else:

            self.item = None

            self.__name = id

            self.__id = id

            self.__attributes_items : list[Attribute] = list()

            self.__relations_items : list[Relation] = list()

            self.__foreign_keys : list[ForeignKey] = list()

    def __read_attributes(self, attribute_items):

        for a in attribute_items:

            attribute = Attribute(a)

            self.__attributes_items.append(attribute)

    def set_relations(self, relations):
        self.__relations_items = relations

    def set_foreign_keys(self, foreign_keys):
        self.__foreign_keys = foreign_keys

    def name(self):
        return self.__name
    
    def id(self):
        return self.__id

    def attributes(self):
        return self.__attributes_items

    def relations(self):
        return self.__relations_items

    def add_attribute(self, attribute):
        self.__attributes_items.append(attribute)

    def edit_attribute_type(self, attribute_name, retype):

        for a in self.__attributes_items:

            if a.name() == attribute_name:
                a.set_type(retype)
                break

    def edit_attribute_name(self, attribute_name, rename):

        for a in self.__attributes_items:

            if a.name() == attribute_name:
                a.set_name(rename)
                break

    def delete_attribute_name(self, attribute_name):

        for i in range(len(self.__attributes_items)):

            if self.__attributes_items[i].name() == attribute_name:
                self.__attributes_items.pop(i)
                break

    # Derivated operations
    def related_entities(self):

        related_entities = []

        for r in self.relations():

            if(r.first_entity() != self):
                related_entities.append(r.first_entity() )

            if(r.second_entity() != self):
                related_entities.append(r.second_entity() )

        return related_entities

    def foreign_keys(self):
        return self.__foreign_keys


    def __str__(self) -> str:
        return "Entity: " + self.name() + " (id = \"" + self.id() + "\", number of attributes = " +str(len(self.attributes())) + ")"