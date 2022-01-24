class Attribute:

    def __init__(self, attribute_item):
        self.attribute_item = attribute_item

        self.name = self.attribute_item.getElementsByTagName("name")[0].childNodes[0].data
        self.type = self.attribute_item.getElementsByTagName("type")[0].childNodes[0].data