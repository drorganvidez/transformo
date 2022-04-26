from core.stm.Action import Action


class Transformation:

    def __init__(self, sdm, item):

        self.__sdm = sdm
        self.item = item

        self.__type = item.getAttribute('type')
        self.__id = item.getAttribute('id')

        self.__actions: list[Action] = list()

        self.__read_actions(item.getElementsByTagName("action"))

    def sdm(self):
        return self.__sdm

    def __read_actions(self, actions):
        
        for a in actions:

            action = Action(sdm = self.__sdm, item = a, transformation_action = self.__type)
            self.__sdm = action.sdm()

            self.__actions.append(action)

    def type(self):
        return self.__type

    def id(self):
        return self.__id

    def actions(self):

        return self.__actions


    def __str__(self) -> str:

        string = "Transformation '{id}' (type {type})\n".format( id = self.__id, type = self.__type)

        return string