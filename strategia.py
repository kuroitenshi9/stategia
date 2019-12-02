class Wojownik:
    def __repr__(self):
        return f'{self.__class__.__name__}: hp=({self.HP}), exp=({self.experience})'
    
    def maszeruj(self, distance):
        self.experience += distance * 0.2
        print(f'{self.__class__.__name__}: Przeszedłem ({distance}) m. Plus {distance * 0.2} do doświadczenia)')
        
class Rycerz(Wojownik):
    def __init__(self):
        self.HP = 60
        self.experience = 0

    # def __repr__(self):
    #     return f'Rycerz: hp=({self.HP}), exp=({self.experience})'

    # def maszeruj(self, distance):
    #     self.experience += distance * 0.2
    #     print(f'Rycerz: Przeszedłem ({distance}) m. Plus {distance * 0.2} do doświadczenia)')
    
    def atakuj(self):
        self.experience += 0.3
        print(f'Rycerz: Machnąłem mieczem')

class Lucznik(Wojownik):
    def __init__(self):
        self.HP = 40
        self.experience = 0
        self.kolczan = 10

    # def __repr__(self):
    #     return f'Łucznik: hp=({self.HP}), exp=({self.experience}, strzały=({self.kolczan}))'

    # def maszeruj(self, distance):
    #     self.experience += distance * 0.2
    #     print(f'Łucznik: Przeszedłem ({distance}) m. Plus {distance * 0.2} do doświadczenia)')
    
    def atakuj(self):
        if self.kolczan > 0:
            self.kolczan -= 1
            self.experience += 0.4
            print(f'Łucznik: wystrzeliłem strzałę')
        else:
            print(f'Łucznik: brak strzał w kołczanie')


def main():
    ry = Rycerz()
    print(ry)
    ry.maszeruj(100)
    ry.atakuj()
    print(ry)
    print("-"*50)
    l = Lucznik()
    print(l)
    l.maszeruj(100)
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    l.atakuj()
    print(l)

if __name__ == '__main__':
    main()
