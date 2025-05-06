# ############################################################
# # #### Filtro Ejercicio3 ######
# ############################################################

def sum(a,b):
   operacion = a+b
   return operacion

def res(a,b):
   operacion = a-b
   return operacion

def multi(a,b):
   operacion = a*b
   return operacion

def div(a,b):
   operacion = a/b
   return operacion
 
numeroUno = float(input("Hola dame un numero"))
operacion = input("Que operacion quieres hacer +,-,*,/")
numeroDos = float(input("Ahora dame otro numero"))

if (operacion == "+"):
    suma = sum(numeroUno,numeroDos)
    print(suma)
    
if (operacion == "-"):
    resta = res(numeroUno,numeroDos)
    print(resta)
    
if (operacion == "*"):
    multiplicacion = multi(numeroUno,numeroDos)
    print(multiplicacion)
    
if (operacion == "/"):
    division = div(numeroUno,numeroDos)
    print(division)