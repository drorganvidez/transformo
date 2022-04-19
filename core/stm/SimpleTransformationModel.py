from xml.dom import minidom

from core.stm.Transformation import Transformation

class SimpleTransformationModel:

    def __init__(self, sdm, file) -> None:
        
        self.__sdm = sdm
        self.__file = file

        doc = minidom.parse(self.__file)

        self.__transformations = []

        self.__read_transformations(doc)

    def __read_transformations(self, doc):
        items = doc.getElementsByTagName('transformation')

        for i in items:
            transformation = Transformation(sdm = self.__sdm, item = i)
            self.__transformations.append(transformation)

    def transformations(self):
        return self.__transformations

    def sdm(self):
        return self.__sdm

    def print(self):
        for t in self.__transformations:
            print("\n" + str(t))

            print("\tActions:")
            for a in t.actions():
                print("\t" + str(a))