import datetime
import time

def definirPrimalidad(num):
    primo = True
    for i in range(3, int(num/2)):
        if num != 2 or num != 3:
            if num % i == 0:
                primo = False
                break
        else:
            if num%2 and num!=2 == 0:
                primo = False
                break
    return primo

num = int(input("Ingrese un número: "))
print ("Tiempo de inicio: "+str(datetime.datetime.now().time()))
inicio = time.time()
primo = definirPrimalidad(num)
final = time.time()
if primo == True:
    print("Es primo")
else:
    print("No es primo")
print ("Tiempo de fin: "+str(datetime.datetime.now().time()))
print  ("Tiempo de ejecución: "+str(final-inicio))