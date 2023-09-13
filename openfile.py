# Read all data
def read_all():
    # Openfile
    f = open("filedata/mydata.txt", "r", encoding="utf8")
    print(f.read())
    f.close()


# Read line by line
def read_line():
    # Openfile
    f = open("filedata/mydata.txt", "r", encoding="utf8")
    for i in range(1,5):
        print(f.readline(), end="")
    f.close()

read_all()
# read_line()