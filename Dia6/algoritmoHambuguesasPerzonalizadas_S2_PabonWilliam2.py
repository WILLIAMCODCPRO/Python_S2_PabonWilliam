# ############################################################
# # #### Algoritmo de Hamburguesas personalizadas ######
# ############################################################

def precioSeleccionado(mensajeUno,mensajeDos,precioUno,precioDos,Preciotres,precio):
   
    print(mensajeUno)
    ingrediente = int(input(mensajeDos))
    
    if (ingrediente == 1):
        precio = precioUno
    elif (ingrediente == 2):
        precio = precioDos
    elif (ingrediente == 3):
        precio = Preciotres
        
    return precio
   
cantidadHamburguesas = int(input("Hola, cuantas Hamburguesa quieres personalizr"))
precioTotal = 0
for i in range(cantidadHamburguesas):
    
    pan = precioSeleccionado("Elije el tipo de pan","1.CENTENO $1000 2.Avena $1500",1000,1500,0,0)
    carne = precioSeleccionado("Elije la cantidad de carne","1.250G $5000 2.300G $7000",5000,7000,0,0)
    pollo = precioSeleccionado("elige la cantidad de pollo", '1: 250G $4500 2: 350G $5500', 4500, 5500, 0,0)
    polloDesmechado = precioSeleccionado("elige la cantidad de pollo desmechado", '1: 250G $6500 2: 350G $7500', 6500, 7500, 0,0)
    tocineta = precioSeleccionado("elige la cantidad de tocineta",  '1: 1 LONJA DE TOCINETA $1500 2: 2 LONJAS DE TOCINETA $2500', 1500, 2500, 0,0)
    papaFrita = precioSeleccionado("elige el tipo de papa frita", '1: A LA FRANCESA $5000 2: EN CASCOS $6000', 5000, 6000, 0,0)
    bebida = precioSeleccionado("elige el tipo de bebida", '1: GASEOSA $5000 2: CERVEZA CLUB COLOMBIA $8000 3: NARANJADA $9000', 5000, 8000, 9000,0)
		
    
    precioTotal = pan + carne + pollo + polloDesmechado + tocineta + papaFrita + bebida + precioTotal  
    
precioTotal = precioTotal + (precioTotal * 0.10) 
print(precioTotal)
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412