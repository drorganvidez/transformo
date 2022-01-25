from SDBMReader import SDBMReader

def main():

    reader_1 = SDBMReader("sdbm/sdbm1.xml")

    reader_1.print()

    reader_2 = SDBMReader("sdbm/sdbm2.xml")

    reader_2.print()


main()