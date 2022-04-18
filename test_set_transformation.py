from core.mysql.MySQLExtractor import MySQLExtractor
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel

def test_set_transformation():

    sdm1 = SimpleDatabaseModel('sdm/sdm1.xml')
    sdm1.print()

    sdm2 = SimpleDatabaseModel('sdm/sdm2.xml')
    sdm2.print()


test_set_transformation()
