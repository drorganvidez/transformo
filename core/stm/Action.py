

class Action:

    def __init__(self, sdm, item) -> None:
        
        self.__sdm = sdm
        self.__item = item

        self.__type = item.getAttribute('type')

        #self.__attribute = self.__item.getElementsByTagName("attribute")[0].childNodes[0].data
        #self.type = self.__item.getElementsByTagName("type")[0].childNodes[0].data

        self.__origin_entity = None

        self.__find_entities(self.__item)

    def __find_entities(self, entity_item):

        element = None

        # if action is type ENTITY TRANSFORMATION

        # if action is type ATTRIBUTE TRANSFORMATION

        # if action is type RELATION TRANSFORMATION

        if(len(self.__item.getElementsByTagName("from")) != 0):
            element = self.__item.getElementsByTagName("from")[0].childNodes[0].data
            print(element)

            entity = self.__sdm.get_entity_by_id(element)
            print(entity)


        '''
        if(self.__item.getElementsByTagName("from") != 0):
            
            '''
        

    def __str__(self) -> str:
        
        string = "Type = {type}".format(type = self.__type)

        return string