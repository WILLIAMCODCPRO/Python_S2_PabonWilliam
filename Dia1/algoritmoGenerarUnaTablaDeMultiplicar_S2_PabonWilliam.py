# ############################################################
# # #### Algoritmo para generar una tabla de multiplicar ######
# ############################################################
 
numeroTabla = int(input("Escribe a que numero le quieres hacer la tabla"))
limiteTabla = int(input("Escribe hasta que numero llegara la tabla seleccionada"))
for i in range(1,limiteTabla + 1,1):
    resultado = i * numeroTabla
    print(str(i) + "*" + str(numeroTabla) + "=" + str(resultado))
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412