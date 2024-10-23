from dragon import Dragon
from fire import FireMixin
from flying import FlyingMixin
from random import randint
class FlyingFireDragon(Dragon, FireMixin, FlyingMixin):
    def __init__(self):
        super().__init__("Deadly Nadder", 20, 2)
    def special_attack(self, opponent):
        move_choice = randint(1,4)
        if move_choice == 1:
            return self.fireball(opponent)
        elif move_choice == 2:
            return self.fireblast(opponent)
        elif move_choice == 3:
            return self.swoop(opponent)
        else:
            return self.windblast(opponent)