from core.SimpleDatabaseModel import SimpleDatabaseModel

def main():

    sdm1 = SimpleDatabaseModel("sdm/sdm1.xml")

    sdm1.print()

    sdm2 = SimpleDatabaseModel("sdm/sdm2.xml")

    sdm2.print()


main()