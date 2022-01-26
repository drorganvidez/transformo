class Relation:

    def __init__(self, item):

        self.item = item

        self.one_1 = None
        self.one_2 = None

        self.many_1 = None
        self.many_2 = None

        self.__get_value(item = item, type = "one")

        self.__get_value(item = item, type = "one")

        self.__get_value(item = item, type = "many")

        self.__get_value(item = item, type = "many")

        # TODO: Lanzar excepción si no hay exactamente dos entidades

    def __check_max_counter(self):
        counter = 0

        if (self.one_1 != None):
            counter = counter + 1

        if (self.one_2 != None):
            counter = counter + 1

        if (self.many_1 != None):
            counter = counter + 1

        if (self.many_2 != None):
            counter = counter + 1

        return counter == 2

    def __get_value(self, item, type):

        if(self.__check_max_counter()):
            return

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


    # TODO: Pasar la lista de entidades, emparejarlas según el id y settear los atributos
    def set_entities(self, entities):
        pass

    def __str__(self) -> str:

        string = "Relation: "
        counter = 0

        if( self.one_1 != None):
            counter = counter + 1
            string = string + "one (" + self.one_1 + ") "
        
        if( self.one_2 != None):
            if (counter == 1):
                string = string + "to "
            counter = counter + 1
            string = string + "one (" + self.one_2 + ") "

        if( self.many_1 != None):
            if (counter == 1):
                string = string + "to "
            counter = counter + 1
            string = string + "many (" + self.many_1 + ") "

        if( self.many_2 != None):
            if (counter == 1):
                string = string + "to "
            counter = counter + 1
            string = string + "many (" + self.many_2 + ") "

        return string