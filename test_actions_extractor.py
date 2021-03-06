from core.main.Migration import Migration
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel
from core.stm.AvailableActionsExtractor import AvailableActionsExtractor

def test():

    A = SimpleDatabaseModel('sdm/A.xml')
    B = SimpleDatabaseModel('sdm/B.xml')

    migration = Migration(A, B, output_database_name = "basemigrada")
    migration.migrate()
    

if __name__ == "__main__":
    
   test()