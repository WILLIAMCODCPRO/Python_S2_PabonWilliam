# ############################################################
# # #### Algoritmo para verificar si un numero es primo ######
# ############################################################
 
contador = 0
num = int(input("Pasame un numero y te digo si es primo o no"))

for i in range(1,num + 1,1):
    if (num % i == 0):
        contador = contador + 1

if (contador == 2):
    print("Es un numero primo")
else:
    print("No es un numero primo")
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412