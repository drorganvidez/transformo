from core.Attribute import Attribute


class Entity:

    def __init__(self, item):
        self.item = item

        self.name = item.getElementsByTagName("name")[0].childNodes[0].data

        self.id = item.getAttribute('id')

        self.attributes_items = []

        self.__read_attributes(item.getElementsByTagName("attribute"))

    def __read_attributes(self, attribute_items):

        for a in attribute_items:

            attribute = Attribute(a)

            self.attributes_items.append(attribute)

    def name(self) -> str:
        return self.name
    
    def id(self) -> str:
        return self.id

    def attributes(self):
        return self.attributes_items

    def __str__(self) -> str:
        return "Entity: " + self.name + " (id = \"" + self.id + "\", number of attributes = " +str(len(self.attributes())) + ")"