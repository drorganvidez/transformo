from core.stm.Action import Action


class Transformation:

    def __init__(self, sdm, item):

        self.__sdm = sdm
        self.item = item

        self.__type = item.getAttribute('type')
        self.__id = item.getAttribute('id')

        self.__actions = []

        self.__read_actions(item.getElementsByTagName("action"))

    def __read_actions(self, actions):
        
        for a in actions:

            action = Action(sdm = self.__sdm, item = a)

            self.__actions.append(action)

    def actions(self):

        return self.__actions


    def __str__(self) -> str:

        string = "Transformation '{id}' (type {type})\n".format( id = self.__id, type = self.__type)

        return string