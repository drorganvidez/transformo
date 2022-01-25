from typing import List
from xml.dom import minidom

from core.Entity import Entity
from core.Relation import Relation

class SDBMReader:

    def __init__(self, file):
        self.file = file
        
        doc = minidom.parse(file)

        self.get_entities(doc)

        self.get_relations(doc)

    def get_entities(self, doc) -> list[Entity]:
        items = doc.getElementsByTagName('entity')
        list_entities = []
        for i in items:
            entity = Entity(i)
            list_entities.append(entity)

        return list_entities

    def get_relations(self, doc) -> list[Relation]:
        items = doc.getElementsByTagName('relation')
        list_relation = []
        for i in items:
            relation = Relation(i)
            list_relation.append(relation)

        return list_relation