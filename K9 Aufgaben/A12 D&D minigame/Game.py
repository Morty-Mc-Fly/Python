import Classes as cl
from Player import Player


class Game():

    def startGame(self):
        name = input("\tPlayer 1 please choose an alias: ")
        p1 = Player(name)

        name = input("\n\tPlayer 2 please choose an alias: ")
        p2 = Player(name)

        self.chooseCharacter(p1)

    def chooseCharacter(player) -> Player:

        print("\t{} please choose a class :")
