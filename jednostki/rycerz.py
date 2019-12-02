from wojownik import Wojownik

class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self.HP = 60
  
    def atakuj(self):
        self.experience += 0.3
        print(f'Rycerz: Machnąłem mieczem')
