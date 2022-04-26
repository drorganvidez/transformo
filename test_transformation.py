from core.scripter.Scripter import Scripter
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.SimpleTransformationModel import SimpleTransformationModel

def test():

    sdm = SimpleDatabaseModel('sdm/sdm1.xml')
    
    stm = SimpleTransformationModel(sdm = sdm, file = "stm/stm.xml")

    scripter = Scripter(stm = stm, output_database = "output_database")
    scripter.generate()

    scripter.sdm().print()

    #sdm.print()
    

if __name__ == "__main__":
    
   test()