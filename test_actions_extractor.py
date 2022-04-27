from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.AvailableAction import AvailableAction
from core.stm.AvailableActionsExtractor import AvailableActionsExtractor
from core.stm.actions.CreateEntityAction import CreateEntityAction

def test():

    A = SimpleDatabaseModel('sdm/sdm1.xml')
    B = SimpleDatabaseModel('sdm/sdm2.xml')

    A.print()
    B.print()

    extractor = AvailableActionsExtractor(sdm_source = A, sdm_target = B)

    extractor.print()
    

if __name__ == "__main__":
    
   test()