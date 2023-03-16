import random


print("-----------------------------------")
print("-----PIEDRA , PAPEL , TIJERA-------")
print("-----------------------------------")


print("MENÚ")
print("1 --->  PIEDRA ")
print("2 --->  PAPEL ")
print("3 --->  TIJERA ")

opcion = int(input("QUE DESEA ESCOJER : "))
a = 1
b = 2
c = 3
d = random.randint(a,b,c)
if a and d==a:
    rta =" EMPATE "
elif a  d==c:
    rta ="GANADOR: PIEDRA "
elif a and d== b:
    rta ="GANADOR: PAPEL "
elif b and d== a:
    rta =" GANADOR: PAPEL "
elif b and d==b:
    rta =" EMPATE "
elif b and d==c:
    rta =" GANADOR: TIJERA "
elif c and d==a:
    rta =" GANADOR: PIEDRA "
elif c and d== b:
    rta = "GANADOR: TIJERA "
elif c and d== c:
    rta =" EMPATE "
else: 
    rta =" NO COLOCASTE BIEN AL OPCION DEL MENÚ "

print(rta)