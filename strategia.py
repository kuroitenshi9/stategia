from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik

rycerze = []
for i in range(4):
    rycerze.append(Rycerz())
print(rycerze)

for rycerz in rycerze:
    rycerz.maszeruj(200)

rycerze.append(Rycerz())

for rycerz in rycerze:
    rycerz.atakuj()

print(rycerze)

lucznicy = []
for i in range(4):
    lucznicy.append(Lucznik())
print(lucznicy)

armia = lucznicy + rycerze
print(armia)

for wojownik in armia:
    wojownik.atakuj()
print(armia)

# def main():
#     ry = Rycerz()
#     print(ry)
#     ry.maszeruj(100)
#     ry.atakuj()
#     print(ry)
#     print("-"*50)
#     l = Lucznik()
#     print(l)
#     l.maszeruj(100)
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     l.atakuj()
#     print(l)

# if __name__ == '__main__':
#     main()
