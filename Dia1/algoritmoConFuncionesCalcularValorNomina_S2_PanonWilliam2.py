# ############################################################
# # #### Algoritmo para calcular valor nomina######
# ############################################################


def total(a,b):
    calcularTotal = a + b
    return calcularTotal

def promedio(a,b):
    calcularPromedio = a/b
    return calcularPromedio

valorHora = 20000
totalSalariosBrutos = 0
promedioSalarioBruto = 0
totalDescuentoEPS = 0
totalDescuentoPension = 0
totalSalarioNeto = 0
promedioSalarioNeto = 0

empleados = int(input("Escoje el numero de empleados"))
for i in range(1,empleados + 1):
    nombreEmpleado = input("Escribe el nombre del empleado")
    horasTrabajadas = int(input("Escibe cuantas horas trabajo el empleado"))
    sueldoBruto = valorHora * horasTrabajadas
    descuentoEPS = sueldoBruto * 0.04
    descuentoPension = sueldoBruto * 0.04
    sueldoNeto = (sueldoBruto) - (descuentoEPS + descuentoPension)
    
    if (i == 1):
        mayorSalarioNeto = sueldoNeto
        mayorNombre = nombreEmpleado
        menorSalarioNeto = sueldoNeto
        menorNombre = nombreEmpleado
        
    if (sueldoNeto > mayorSalarioNeto):
        mayorSalarioNeto = sueldoNeto
        mayorNombre = nombreEmpleado
        
    if (sueldoNeto < menorSalarioNeto):
         menorSalarioNeto = sueldoNeto
         menorNombre = nombreEmpleado
         
    print(nombreEmpleado + " " + "Sueldo bruto:" + "$" + str(sueldoBruto) + " " + "Descuento EPS:" + "$" + str(descuentoEPS) + " " + "Descuento pension:" + "$" + str(descuentoPension) + " " + "Sueldo Neto:" + "$" + str(sueldoNeto))
    totalSalariosBrutos = total(sueldoBruto,totalSalariosBrutos)
    promedioSalarioBruto = promedio(totalSalariosBrutos,i)
    totalDescuentoEPS = total(descuentoEPS,totalDescuentoEPS)
    totalDescuentoPension = total(descuentoPension,totalDescuentoPension)
    totalSalarioNeto = total(sueldoNeto,totalSalarioNeto)
    promedioSalarioNeto = promedio(totalSalarioNeto,i)
    
print("Total de salarios brutos" + "$" + str(totalSalariosBrutos))
print("Total descuento EPS" + "$" + str(totalDescuentoEPS))
print("Total descuento pension" + "$" + str(totalDescuentoPension))
print("Total de salarios netos" + "$" + str(totalSalarioNeto))
print("El mayor salario neto es" + mayorNombre + "$" + str(mayorSalarioNeto))
print("El mayor salario neto es" + menorNombre + "$" + str(menorSalarioNeto))
print("El promedio del salario Bruto es" + "$" + str(promedioSalarioBruto))
print("El promedio del salrio Neto es" + "$" + str(promedioSalarioNeto))
    
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412