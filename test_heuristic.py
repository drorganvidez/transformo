from core.heuristic.Heuristic import Heuristic
from core.main.Migration import Migration
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel


def test():

    A = SimpleDatabaseModel('sdm/A.xml')
    B = SimpleDatabaseModel('sdm/B.xml')

    migration = Migration(A, B, output_database_name = "basemigrada")
    migration.heuristic_migrate()
    

if __name__ == "__main__":
    
   test()