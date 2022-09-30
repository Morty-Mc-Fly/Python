
import random


loge = [["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
        ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"]]

room = [["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
        ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
        ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
        ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
        ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"],
        ["[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]", "[  ]"]]


def assignLogePlaces(loge):
    for x in range(len(loge)):
        for y in range(len(loge[x])):
            ran = random.randint(0, 1)
            if ran == 1:
                loge[x][y] = "[oo]"
    return loge


def assignRoomPlaces(room):
    for x in range(len(room)):
        for y in range(len(room[x])):
            ran = random.randint(0, 1)
            if ran == 1:
                room[x][y] = "[oo]"
    return room


def printseats(arr):
    for x in range(len(arr)):
        print("")
        for y in range(len(arr[x])):
            print(arr[x][y], end='')
    print("")


def printscreen():
    screen = ["____", "____", "___", "____",
              "____", "____", "____", "____", "_____"]
    for x in range(len(screen)):
        print(screen[x], end='')


loge = assignLogePlaces(loge)

room = assignRoomPlaces(room)

printseats(loge)
print("")
printseats(room)
printscreen()
