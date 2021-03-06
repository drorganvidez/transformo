from core.mysql.MySQLExtractor import MySQLExtractor
from core.sdm.SimpleDatabaseModel import SimpleDatabaseModel

def test_recursion():

    sdm1 = SimpleDatabaseModel("sdm/sdm1.xml")

    for e in sdm1.entities():
        print(e)

        for r in e.relations():

            print(r.first_entity())
            print(r)

            for r2 in r.first_entity().relations():
                print("r2", r2)

                print("r2 first_entity", r2.first_entity())

                for r3 in r2.first_entity().relations():
                    print("r3", r3)   

                    print("r3 first_entity", r3.first_entity())

        print()

def test_properties():
    
    sdm1 = SimpleDatabaseModel("sdm/sdm1.xml")

    for e in sdm1.entities():
        print(e)

        print("related_entities")
        for re in e.related_entities():

            print("\t"+str(re))

        print("end related_entities")
        print()

def test_mysql_extractor():

    mysql_extractor = MySQLExtractor()

    

    mysql_extractor.extract()

    for table in mysql_extractor.tables():
        print("Name: " + table.name())
        for key in table.keys():
            print(key)
    mysql_extractor.generate_simple_database_model(output = "example.xml")

    sdm = SimpleDatabaseModel('sdm/example.xml')

    sdm.print()


#test_recursion()
#test_properties()

test_mysql_extractor()
