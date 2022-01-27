from core.Attribute import Attribute


class Entity:

    def __init__(self, item):
        self.item = item

        self.__name = item.getElementsByTagName("name")[0].childNodes[0].data

        self.__id = item.getAttribute('id')

        self.__attributes_items = []

        self.__read_attributes(item.getElementsByTagName("attribute"))

        self.__relations_items = []

    def __read_attributes(self, attribute_items):

        for a in attribute_items:

            attribute = Attribute(a)

            self.__attributes_items.append(attribute)

    def set_relations(self, relations):
        self.__relations_items = relations

    def name(self):
        return self.__name
    
    def id(self):
        return self.__id

    def attributes(self):
        return self.__attributes_items

    def relations(self):
        return self.__relations_items

    # Derivated operations
    def related_entities(self):

        related_entities = []

        for r in self.relations():

            if(r.first_entity() != self):
                related_entities.append(r.first_entity() )

            if(r.second_entity() != self):
                related_entities.append(r.second_entity() )

        return related_entities


    def __str__(self) -> str:
        return "Entity: " + self.name() + " (id = \"" + self.id() + "\", number of attributes = " +str(len(self.attributes())) + ")"