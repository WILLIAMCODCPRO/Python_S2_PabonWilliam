# ############################################################
# # #### Algoritmo de Hamburguesas personalizadas ######
# ############################################################
 
cantidadHamburguesas = int(input("Hola, cuantas Hamburguesa quieres personalizr"))
precioTotal = 0
for i in range(cantidadHamburguesas):
    print("Elije el tipo de pan")
    pan = int(input("1.CENTENO $1000 2.Avena $1500"))
    
    if (pan == 1):
        precioTotal = precioTotal + 1000
    elif (pan == 2):
        precioTotal = precioTotal + 1500
        
    print("Elije la cantidad de carne")
    carne = int(input("1.250G $5000 2.300G $7000"))
    
    if (carne == 1):
        precioTotal = precioTotal + 5000
    elif (carne == 2):
        precioTotal = precioTotal + 7000
        
    print("Elije la cantidad de pollo")
    pollo = int(input("1.250G $4500 2.350G $5500"))
    
    if (pollo == 1):
        precioTotal = precioTotal + 4500
    elif (pollo == 2):
        precioTotal = precioTotal + 5500
        
    print("Elije la cantidad de pollo desmechado")
    polloDesmechado = int(input("1.250G $6500 2.350G $7500"))
    
    if (polloDesmechado == 1):
        precioTotal = precioTotal + 6500
    elif (polloDesmechado == 2):
        precioTotal = precioTotal + 7500
        
    print("Elije la cantidad de tocineta que quieres")
    tocineta = int(input("1. 1 LONJA DE TOCINETA $1500 2. 2 LONJAS DE TOCINETA $2500"))
    
    if (tocineta == 1):
        precioTotal = precioTotal + 1500
    elif (tocineta == 2):
        precioTotal = precioTotal + 2500
        
    print("Elije el tipo de papa frita que quieres")
    papaFrita = int(input("1. A LA FRANCESA $5000 2. EN CASCOS $6000"))
    
    if (papaFrita == 1):
        precioTotal = precioTotal + 5000
    elif (papaFrita == 2):
        precioTotal = precioTotal + 6000
        
    print("Elije tu bebida")
    bebida = int(input("1. GASEOSA $5000 2. CERVEZA CLUB COLOMBIA $8000 3. NARANJADA $9000"))
    
    if (bebida == 1):
        precioTotal = precioTotal + 5000
    elif (bebida == 2):
        precioTotal = precioTotal + 8000
    elif (bebida == 3):
        precioTotal = precioTotal + 9000
        
precioTotal = precioTotal + (precioTotal * 0.10) 
print("El precio total a pagar es:"+"$"+str(precioTotal))
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412