from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.SimpleTransformationModel import SimpleTransformationModel

def main():

    sdm = SimpleDatabaseModel("sdm/sdm1.xml")
    sdm.print()

    stm = SimpleTransformationModel(sdm = sdm, file = "stm/stm.xml")
    stm.print()
    

if __name__ == "__main__":
   main()