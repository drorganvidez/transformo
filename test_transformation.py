from core.stm.SimpleTransformationModel import SimpleTransformationModel

def test():
    
    stm = SimpleTransformationModel("stm/stm.xml")

    for t in stm.transformations():
        print(t)

if __name__ == "__main__":
   test()