# ############################################################
# # #### Filtro Ejercicio4 ######
# ############################################################
 

def convertirABinario(numero):
    resultado = ""
    if numero == 0:
        return "0"
    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado
        numero = numero // 2
    return resultado


def convertirADecimal(binario):
    potencia = 1
    resultado = 0
    i = len(binario) - 1
    while i >= 0:
        digito = int(binario[i])
        resultado = resultado + digito * potencia
        potencia = potencia * 2
        i = i - 1
    return resultado


seguir = "si"

while seguir == "si":
    conversion = input("¿Quieres convertir un número a binario o a decimal?")
   
    if conversion == "binario":
        numero = int(input("Escribe el número decimal: "))
        numeroBinario = convertirABinario(numero)
        print("El número en binario es:", numeroBinario)

    elif conversion == "decimal":
        binario = input("Escribe el número binario: ")
        numeroDecimal = convertirADecimal(binario)
        print("El número en decimal es:", numeroDecimal)

    seguir = input("Quieres seguir convirtiendo numeros?")

print("Entendido vuelve pronto")


    
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412