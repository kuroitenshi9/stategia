class Wojownik:
    def __init__(self):
        self.experience = 0
 

    def __repr__(self):
        return f'{self.__class__.__name__}: hp=({self.HP}), exp=({self.experience})'
    
    def maszeruj(self, distance):
        self.experience += distance * 0.2
        print(f'{self.__class__.__name__}: Przeszedłem ({distance}) m. Plus {distance * 0.2} do doświadczenia)')

        