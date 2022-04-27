from core.main.Migration import Migration
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.AvailableActionsExtractor import AvailableActionsExtractor

def test():

    A = SimpleDatabaseModel('sdm/sdm1.xml')
    B = SimpleDatabaseModel('sdm/sdm2.xml')

    migration = Migration(A, B, output_database = "basemigrada")
    migration.migrate()
    

if __name__ == "__main__":
    
   test()