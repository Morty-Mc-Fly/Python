from Game import Game as g
import sys


def main():
    inp = input("\tDo you want to start the Game ? (yes/no) : ")
    print("")
    if inp.lower() == "yes":
        g.startGame()
    elif inp.lower() == "no":
        sys.exit("\tClosed Game")
    else:
        print("\tinvalid input!")
        main()


if __name__ == '__main__':
    main()
