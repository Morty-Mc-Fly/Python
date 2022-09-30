import random
import time


def getRandom():
    print("\tGenerating Number. . .")
    __ran = random.randint(0, 100)
    print("\tGenerated number")
    print(__ran)
    return __ran


def turn(index):
    return int(input("\n\tTurn {} : ".format(index)))


def startSearchGame():
    __number = getRandom()
    for x in range(0, 5):

        inp = turn(x+1)
        if inp == __number:

            print("\tYou Won!!")
            break

        elif inp > __number:

            if x == 4:
                print("\tYou Lost!!! \n\tThe number was {}".format(__number))
                break
            else:
                print("\tGo Lower")

        elif inp < __number:
            if x == 4:
                print("\tYou Lost!!! \n\tThe number was {}".format(__number))
                break
            else:
                print("\tGo Higher")


def randomInRange(ind, end):
    if ind < end:
        __ran = random.randint(ind, end)
        print("Picked : ", __ran)
        return __ran
    else:
        __ran = random.randint(end, ind)
        print("Picked : ", __ran)
        return __ran


def startComputerSearch():
    __number = int(input("Input a number: "))

    high = 100
    low = 0

    for x in range(0, 5):
        inp = randomInRange(high, low)
        print(low, high)

        if inp == __number:

            print("\tYou Won!!")
            break

        elif inp > __number:
            high = inp

            if x == 4:
                print("\tYou Lost!!! \n\tThe number was {}".format(__number))
                break
            else:
                print("\tGo Lower")

        elif inp < __number:
            low = inp

            if x == 4:
                print("\tYou Lost!!! \n\tThe number was {}".format(__number))
                break
            else:
                print("\tGo Higher")


# startSearchGame()
startComputerSearch()
