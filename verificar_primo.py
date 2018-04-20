from Primal import *

num = int(input("Ingrese un número: "))
#print ("Tiempo de inicio: "+str(datetime.datetime.now().time()))
inicio = time.time()
primo = primalidad.definirPrimalidad(num)
final = time.time()
if primo == True:
    print("Es primo")
else:
    print("No es primo")
#print ("Tiempo de fin: "+str(datetime.datetime.now().time()))
print  ("Tiempo de ejecución: "+str((final-inicio)))