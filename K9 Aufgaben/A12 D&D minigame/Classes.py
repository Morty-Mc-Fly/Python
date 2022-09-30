from Abillities import Abillity as abil
from Dice import Die as die


class CharClass():
    def __init__(self, cname, init, hp):
        self.name = cname
        self.init = init
        self.healthpoints = hp

    def charToString(self):
        print("\tA mighty {}\n\t\n\tYou have {} HP\n\tand an initative of {}".format(
            self.role, self.healthpoints, self.init))
    pass

    def abilToString(self):
        print("\tThe {} has the abillities:")
        for x in range(len(self.adArr)):
            print("{} {}".format(self.abArr[x].name))
    pass


class Mage(CharClass):

    def __init__(self, name):
        super().__init__(name, 1+die.throwD6(), 7+die.throwD6())
        self.role = "Mage"
        self.fireball = abil("Fireball")
        self.magicmissile = abil("Magic missile")
        self.mirrorimage = abil("Mirror image")
        self.smallpotion = abil("Small health potion")
        self.abArr = [self.fireball, self.magicmissile,
                      self.mirrorimage, self.smallpotion]


class Scoundel(CharClass):

    def __init__(self, name):
        super().__init__(name, 2+die.throwD10(), 5+die.throwD8())
        self.role = "Scoundrel"
        self.sneakattack = abil("Sneak attack")
        self.daggerattack = abil("Dagger attack")
        self.dirtystrike = abil("Dirty strike")
        self.healingpotion = abil("Health potion")
        self.abArr = [self.sneakattack, self.daggerattack,
                      self.dirtystrike, self.healingpotion]


class Warrior(CharClass):

    def __init__(self, name):
        super().__init__(name, die.throwD8(), 10+die.throwD10())
        self.role = "Warrior"
        self.swordattack = abil("Sword attack")
        self.shieldblock = abil("Shield block")
        self.healingpotion = abil("Health potion")
        self.abArr = [self.swordattack, self.shieldblock, self.healingpotion]
