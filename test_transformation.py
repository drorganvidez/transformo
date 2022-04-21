from core.generator.Generator import Generator
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.SimpleTransformationModel import SimpleTransformationModel

def test():

    sdm = SimpleDatabaseModel('sdm/sdm1.xml')
    
    stm = SimpleTransformationModel(sdm = sdm, file = "stm/stm.xml")

    for t in stm.transformations():
        print(t)

        print("\tactions")
        for a in t.actions():
            print("\t"+str(a))

        print("\n")


    generator = Generator(stm = stm)
    generator.generate()

    sdm.print()
    

if __name__ == "__main__":
    
   test()