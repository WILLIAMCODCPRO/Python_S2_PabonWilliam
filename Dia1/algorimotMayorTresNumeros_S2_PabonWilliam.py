# ############################################################
# # #### Algoritmo para hallar el mayor de tres numeros ######
# ############################################################
 
numeroUno = int(input("Hola pasame un numero"))
numeroDos = int(input("Pasa otro numero"))
numeroTres = int(input("Uno mas"))

if numeroUno > numeroDos and numeroUno > numeroTres:
    print("El número mayor es: " + str(numeroUno))
elif numeroDos > numeroUno and numeroDos > numeroTres:
    print("El número mayor es: " + str(numeroDos))
else:
    print("El número mayor es: " + str(numeroTres))
 
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412