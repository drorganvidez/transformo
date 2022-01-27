from typing import List
from xml.dom import minidom

from core.Entity import Entity
from core.Relation import Relation

class SimpleDatabaseModel:

    def __init__(self, file):
        self.file = file
        
        doc = minidom.parse(file)

        self.entities_items = []
        self.relations_items = []

        self.__read_entities(doc)
        self.__read_relations(doc)

        self.match_relation_and_entities()

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

    def relations(self):
        return self.relations_items

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