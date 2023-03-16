import random


print("-----------------------------------")
print("-----PIEDRA , PAPEL , TIJERA-------")
print("-----------------------------------")


print("MENÚ")
print("1 --->  PIEDRA ")
print("2 --->  PAPEL ")
print("3 --->  TIJERA ")

opcion = int(input("QUE DESEA ESCOJER : "))

maquina = random.randint(a,b,c)
b = 2
c = 3
a = 1
if a and maquina==a:
    rta =" EMPATE "
elif a == maquina==c:
    rta ="GANADOR: PIEDRA "
elif a and maquina== b:
    rta ="GANADOR: PAPEL "
elif b and maquina== a:
    rta =" GANADOR: PAPEL "
elif b and maquina==b:
    rta =" EMPATE "
elif b and maquina==c:
    rta =" GANADOR: TIJERA "
elif c and maquina==a:
    rta =" GANADOR: PIEDRA "
elif c and maquina== b:
    rta = "GANADOR: TIJERA "
elif c and maquina== c:
    rta =" EMPATE "
else: 
    rta =" NO COLOCASTE BIEN AL OPCION DEL MENÚ "

print("-----------------------")
print("-------GANADOR---------")
print("--------, " , rta)