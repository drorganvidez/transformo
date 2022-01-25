from SDBMReader import SDBMReader

def main():

    reader = SDBMReader("sdbm/sdbm1.xml")

    for e in reader.entities():
        print(e)

        for attr in e.attributes():
            print(attr)

    for r in reader.relations():
        print(r)


main()