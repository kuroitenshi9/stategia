from wojownik import Wojownik

class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self.HP = 40
        self.kolczan = 10

    def atakuj(self):
        if self.kolczan > 0:
            self.kolczan -= 1
            self.experience += 0.4
            print(f'Łucznik: wystrzeliłem strzałę')
        else:
            print(f'Łucznik: brak strzał w kołczanie')
