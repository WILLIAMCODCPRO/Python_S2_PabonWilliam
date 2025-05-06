# ############################################################
# # #### Algoritmo para generar la serie de Fibonacci ######
# ############################################################
 
primerNumero = 0
segundoNumero = 1
terminoSecuencia = int(input("Pasame el termino hasta el cual quieres generar la serie de Fibonacci"))
for i in range (1,terminoSecuencia,1):
    if (i==1):
        print(primerNumero)
    if (i==2):
        print(segundoNumero)
    else:
     tercerNumero = primerNumero + segundoNumero
     print(tercerNumero)
     primerNumero = segundoNumero
     segundoNumero = tercerNumero   
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412