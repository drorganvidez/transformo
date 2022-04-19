from typing import List
from xml.dom import minidom

from core.sdm.Entity import Entity
from core.sdm.ForeignKey import ForeignKey
from core.sdm.Relation import Relation

class SimpleDatabaseModel:

    def __init__(self, file):
        self.file = file
        
        doc = minidom.parse(file)

        self.entities_items: list[Entity] = list()
        self.relations_items = []

        self.__read_entities(doc)
        self.__read_relations(doc)

        self.match_relation_and_entities()

        self.detect_foreign_keys()

    def __read_entities(self, doc):
        items = doc.getElementsByTagName('entity')

        for i in items:
            entity = Entity(i)
            self.entities_items.append(entity)

    def entities(self):
        return self.entities_items

    def __read_relations(self, doc) -> list[Relation]:
        items = doc.getElementsByTagName('relation')

        for i in items:
            relation = Relation(i)
            self.relations_items.append(relation)

    def match_relation_and_entities(self):

        for r in self.relations_items:
            r.set_entities(self.entities_items)

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

    def relations(self):
        return self.relations_items

    def get_entity_by_id(self, id) -> Entity:
        res = None

        for e in self.entities():
            if(e.id() == id):
                res = e
                break

        return res

    def print(self) -> str:

        print()

        print(self.file)
        
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