def countingStars(int):
    print("Number {} equals :>".format(int))
    str = ""
# counting -> int
    for i in range(1, int+1):
        for x in range(0, i):

            str = str + "* "
        print(str)

        str = ""
# counting -> 0
    for i in reversed(range(1, int)):
        for x in reversed(range(0, i)):

            str = str + "* "
        print(str)
        str = ""


countingStars(10)

countingStars(5)
