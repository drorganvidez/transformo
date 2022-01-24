from core.Attribute import Attribute


class Entity:

    def __init__(self, item):
        self.item = item

        self.name = item.getElementsByTagName("name")[0].childNodes[0].data

        print("name: ", self.name)

        self.get_attributes(item.getElementsByTagName("attribute"))

    def get_attributes(self, attribute_items) -> list[Attribute]:

        list_attribute = []

        for a in attribute_items:

            attribute = Attribute(a)

            list_attribute.append(attribute)

        return list_attribute