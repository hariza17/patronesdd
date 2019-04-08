from prototype.prototype_1 import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, level):

        self.unit_type = "Knight"
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, "r") as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Life: {0}\n" \
               "Speed: {1}\n" \
               "Attack Power: {2}\n" \
               "Attack Range: {3}\n" \
               "Weapon: {4}".format(self.life, self.speed, self.attack_power, self.attack_range, self.weapon)

    def clone(self):
        return deepcopy(self)
