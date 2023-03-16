import random

aleatorio = random.randrange(0, 3)
eligePc = ""
print("1 -------> Piedra ")
print("2 -------> Papel ")
print("3 -------> Tijera ")
opcion = int(input("Que eliges: "))

if opcion == 1:
    de = "piedra"
elif opcion == 2:
    de = "papel"
elif opcion == 3:
    de = "tijera"
print("Tu eliges: ", de)

if aleatorio == 0:
    eligePc = "piedra"
elif aleatorio == 1:
    eligePc = "papel"
elif aleatorio == 2:
    eligePc = "tijera"
print("PC eligió: ", eligePc)
print("...")
if eligePc == "piedra" and de == "papel":
    print("Ganaste, papel envuelve piedra")
elif eligePc == "papel" and de == "tijera":
    print("Ganaste, Tijera corta papel")
elif eligePc == "tijera" and de == "piedra":
    print("Ganaste, Piedra pisa tijera")
if eligePc == "papel" and de == "piedra":
    print("perdiste, papel envuelve piedra")
elif eligePc == "tijera" and de == "papel":
    print("perdiste, Tijera corta papel")
elif eligePc == "piedra" and de == "tijera":
    print("perdiste, Piedra pisa tijera")
elif eligePc == de:
    print("empate")