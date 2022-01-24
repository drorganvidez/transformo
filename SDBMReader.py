from typing import List
from xml.dom import minidom

from core.Entity import Entity

class SDBMReader:

    def __init__(self, file):
        self.file = file
        
        doc = minidom.parse(file)

        self.get_entities(doc)

    def get_entities(self, doc) -> list[Entity]:
        items = doc.getElementsByTagName('entity')
        list_entities = []
        for i in items:
            entity = Entity(i)
            list_entities.append(entity)

        return list_entities
        