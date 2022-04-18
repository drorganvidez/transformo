from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.SimpleTransformationModel import SimpleTransformationModel

def test():

    sdm = SimpleDatabaseModel('sdm/example.xml')
    sdm.print()
    
    stm = SimpleTransformationModel(sdm = sdm, file = "stm/stm.xml")

    for t in stm.transformations():
        print(t)

if __name__ == "__main__":
   test()