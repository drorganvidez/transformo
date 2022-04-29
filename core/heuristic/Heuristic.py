from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel


class Heuristic:

    def __init__(self, sdm_source : SimpleDatabaseModel, sdm_target: SimpleDatabaseModel) -> None:

        self._A = sdm_source
        self._B = sdm_target

    def calculate(self):

        heuristic = 0

        # ¿qué entidades o atributos "sobran" en la base de datos final?
        for eB in self._B.entities():

            # entidades que faltan en la base final
            if not self._A.contains_entity(eB):

                heuristic = heuristic + 1 # cost for create entity
                heuristic = heuristic + len(eB.attributes()) # cost for create every attribute

            else:

                eA = self._A.get_entity_by_id(eB.id())

                for attA in eA.attributes():

                    if eB.contains_attribute_by_name(attA.name()):

                        attB = eB.get_attribute_by_name(attA.name())

                        if not attA.type() == attB.type():

                            # atributos de A que están en B pero el tipo no es el mismo

                            heuristic = heuristic + 1

                    else:

                        # atributos de la entidad de A que "sobran" en la entidad de B 

                        heuristic = heuristic + 1

                for attB in eB.attributes():

                    if eA.contains_attribute_by_name(attB.name()):

                        attA = eA.get_attribute_by_name(attB.name())

                        if not attA.type() == attB.type():

                            heuristic = heuristic + 1

                    else:

                        heuristic = heuristic + 1
                

        # ¿qué entidades o atributos "sobran" en la base de datos final?
        for eA in self._A.entities():

            # entidades que sobran de la base final
            if not self._B.contains_entity(eA):

                heuristic = heuristic + 1 # cost for delete entity
                heuristic = heuristic + len(eB.attributes()) # cost for delete every attribute

        return heuristic