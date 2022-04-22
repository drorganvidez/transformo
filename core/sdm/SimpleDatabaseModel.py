from copy import copy
from typing import List
from xml.dom import minidom
from core.sdm.Attribute import Attribute

from core.sdm.Entity import Entity
from core.sdm.ForeignKey import ForeignKey
from core.sdm.Relation import Relation

class SimpleDatabaseModel:

    def __init__(self, file):
        self.__file = file
        
        doc = minidom.parse(self.__file)

        self.entities_items: list[Entity] = list()
        self.relations_items: list[Relation] = list()

        self.__read_entities(doc)
        self.__read_relations(doc)

        self.match_relations_and_entities()

        self.detect_foreign_keys()

    def __read_entities(self, doc) -> None:
        items = doc.getElementsByTagName('entity')

        for i in items:
            entity = Entity(i)
            self.entities_items.append(entity)

    def entities(self) -> list[Entity]:
        return self.entities_items

    def __read_relations(self, doc) -> None:
        items = doc.getElementsByTagName('relation')

        for i in items:
            relation = Relation(i)
            self.relations_items.append(relation)

    def match_relations_and_entities(self) -> None:

        self.match_relations()

        self.match_entities()

    def match_relations(self) -> None:

        for r in self.relations_items:
            r.set_entities(self.entities_items)

    def match_entities(self) -> None:

        for e in self.entities_items:
            e.set_relations(self.relations_items)

    def detect_foreign_keys(self):

        for e in self.entities_items:

            foreign_keys : list[ForeignKey] = list()

            for r in e.relations():
                if(r.second_entity().id() == e.id()):
                    foreign_key = ForeignKey(r.first_entity())
                    foreign_keys.append(foreign_key)

            e.set_foreign_keys(foreign_keys)

    def relations(self) -> list[Relation]:
        return self.relations_items

    def get_entity_by_id(self, id) -> Entity:
        res = None

        for e in self.entities():
            if(e.id() == id):
                res = e
                break

        return res

    def add_entity(self, entity_name):

        entity = Entity(static = True, id = entity_name)
        self.entities_items.append(entity)

    def add_relation(self, relations):

        first_entity = self.get_entity_by_id(relations[0].getElementsByTagName("entity")[0].childNodes[0].data)
        second_entity = self.get_entity_by_id(relations[1].getElementsByTagName("entity")[0].childNodes[0].data)
        first_entity_cardinality = relations[0].getElementsByTagName("cardinality")[0].childNodes[0].data
        second_entity_cardinality = relations[1].getElementsByTagName("cardinality")[0].childNodes[0].data

        # create relation
        relation = Relation(
            static = True, 
            first_entity = first_entity, 
            second_entity = second_entity, 
            first_entity_cardinality = first_entity_cardinality, 
            second_entity_cardinality = second_entity_cardinality)

        # add to list
        self.relations_items.append(relation)

        # matching between entities
        self.match_entities()

    def add_attribute(self, entity, attribute_name, attribute_type):

        attribute = Attribute(static = True, attribute_name = attribute_name, attribute_type = attribute_type)

        entity.add_attribute(attribute = attribute)

    def edit_attribute_type(self, entity, attribute_name, retype):

        entity.edit_attribute_type(attribute_name = attribute_name, retype = retype)

    def edit_attribute_name(self, entity, attribute_name, rename):

        entity.edit_attribute_name(attribute_name = attribute_name, rename = rename)

    def delete_attribute(self, entity, attribute_name):

        entity.delete_attribute_name(attribute_name = attribute_name)

    def file(self) -> str:
        return self.__file


    def print(self) -> str:

        print()

        print(self.__file)
        
        for e in self.entities():

            print(e)

            print("\n\t-- Attributes --")

            for attr in e.attributes():
                print("\t" + str(attr))

            print()

            print("\t-- Related entities --")

            for re in e.related_entities():
                print("\t" + str(re))

            print()

        print("-- All relations --")
        for r in self.relations():
            print(r)

        print()