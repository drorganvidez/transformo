class Relation:

    def __init__(self, item):

        self.item = item

        self.one_1 = None
        self.one_2 = None

        self.many_1 = None
        self.many_2 = None

        self.__get_value(item = item, attribute = "one_1", type = "one")
        print("one_1", self.one_1)

        self.__get_value(item = item, attribute = "one_2", type = "one")
        print("one_2", self.one_2)

        self.__get_value(item = item, attribute = "many_1", type = "many")
        print("many_1", self.many_1)

        self.__get_value(item = item, attribute = "many_2", type = "many")
        print("many_2", self.many_2)

    def __get_value(self, item, attribute, type):

        ones_manies = item.getElementsByTagName(type)

        if len(ones_manies) == 2:

            if type == "one":
                setattr(self, "one_1", item.getElementsByTagName(type)[0].getAttribute('id') )
                setattr(self, "one_2", item.getElementsByTagName(type)[1].getAttribute('id') )

            if type == "many":
                setattr(self, "many_1", item.getElementsByTagName(type)[0].getAttribute('id') )
                setattr(self, "many_2", item.getElementsByTagName(type)[1].getAttribute('id') )

        if len(ones_manies) == 1:

            if type == "one":
                setattr(self, "one_1", item.getElementsByTagName(type)[0].getAttribute('id') )

            if type == "many":
                setattr(self, "many_1", item.getElementsByTagName(type)[0].getAttribute('id') )

