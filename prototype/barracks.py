from prototype.knight import Knight
from prototype.archer import Archer


class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "Archer": {
                1: Archer(1),
                2: Archer(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    archer1 = barracks.build_unit("Archer", 1)

    knight2 = barracks.build_unit("knight", 2)
    archer2 = barracks.build_unit("Archer", 2)

    print("[knight1] {}".format(knight1))
    print("\n[archer1] {}".format(archer1))

    print("\n[knight2] {}".format(knight2))
    print("\n[archer2] {}".format(archer2))
