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

        # TODO: Emparejar relaciones y entidades.
        # Desde una relación, debo poder consultar ambas entidades y la cardinalidad
        # Desde una entidad, debo poder consultar la relación con el resto de entidades

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

    def relations(self):
        return self.relations_items

    def print(self) -> str:

        print()

        print(self.file)
        
        for e in self.entities():
            print(e)

            for attr in e.attributes():
                print("\t" + str(attr))

            print()

        for r in self.relations():
            print(r)

        print()