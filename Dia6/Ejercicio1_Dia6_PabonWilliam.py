# #####################
# # #### Dia 6 ########
# #####################

listaPersonas = []
programa = True

while (programa):
    
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    
    if (opcionUsuario == 1):
        diccionarioVacio = {}
        diccionarioVacio["id"] = input("Ingre un ID para la persona")
        diccionarioVacio["Nombre"] = input("Ingrese el nombre de la persona")
        diccionarioVacio["Apellido"] = input("Ingrese el apellido de la persona")
        diccionarioVacio["Edad"] = input("Ingrese la edad de la persona")
        diccionarioVacio["Telefono"] = []
        
        cantidadTelefonos = int(input("¿Cuántos teléfonos desea ingresar?: "))
        for i in range(cantidadTelefonos):
        
         print("Ahora ingresa el telefono de la persona")
         telefonos = {}
         print(f"Teléfono #{i+1}")
         telefonos["codigo"] = input("Ingrese el codigo postal del telefono")
         telefonos["numero"] = input("Ingrese el numero de telefono")
         telefonos["tipo"] = input("¿Es un telefono de trabajo o personal") 
         diccionarioVacio["Telefono"].append(telefonos)
        
        listaPersonas.append(diccionarioVacio)
        print("Felicidades creaste una persona")
        
    elif (opcionUsuario == 2):
        for i in range(len(listaPersonas)):
            print("#################")
            print("######Persona", i + 1, "#######")
            print("#################")
            print("ID:", listaPersonas[i]["id"])
            print("Nombre:", listaPersonas[i]["Nombre"])
            print("Apellido:", listaPersonas[i]["Apellido"])
            print("Edad:", listaPersonas[i]["Edad"])
            
            for q in range(len(listaPersonas[i]["Telefono"])):
                  print("---------------------------")
                  print("Teléfono #", q+1, ":")
                  print("### --- codigo", listaPersonas[i]["Telefono"][q]["codigo"])
                  print("### --- numero", listaPersonas[i]["Telefono"][q]["numero"])
                  if listaPersonas[i]["Telefono"][q]["tipo"] == "personal":
                    print("#### - Tipo: Es su número Personal")
                  else:
                    print("#### - Tipo: Es su número de Trabajo")
                    print("---------------------------") 
    elif(opcionUsuario==3):
     print("#################")
     print("#### Mostrar Persona Individual ####")
     print("#################")
    
     idBuscado = input("Ingrese el ID de la persona a buscar: ")

     personaEncontrada = None  

     for persona in listaPersonas:
         if persona["id"] == idBuscado:
             personaEncontrada = persona
             break
         else:
          print("No se encontró ninguna persona con ese ID.")
          
     if (personaEncontrada):
         print("ID:", personaEncontrada["id"])
         print("Nombre:", personaEncontrada["Nombre"])
         print("Apellido:", personaEncontrada["Apellido"])
         print("Edad:", personaEncontrada["Edad"])
        
         for i, tel in enumerate(personaEncontrada["Telefono"]):
            print("---------------------------")
            print("Teléfono#", i+1)
            print("#### - Código:", tel["codigo"])
            print("#### - Número:", tel["numero"])
            if tel["tipo"] == "personal":
                print("#### - Tipo: Es su número Personal")
            else:
                print("#### - Tipo: Es su número de Trabajo")
            print("---------------------------")
    elif (opcionUsuario == 4):
     print("#################")
     print("#### Actualizar Persona ####")
     print("#################")
     idBuscado = input("Ingrese el ID de la persona que desea actualizar: ")
     personaEncontrada = None

     for persona in listaPersonas:
        if persona["id"] == idBuscado:
            personaEncontrada = persona
            break
        else:
         print("No se encontró una persona con ese ID.")    
         
     if (personaEncontrada):
        nuevoNombre = input("Ingrese el nuevo nombre (actual: " + personaEncontrada["Nombre"] + "): ")
        nuevoApellido = input("Ingrese el nuevo apellido (actual: " + personaEncontrada["Apellido"] + "): ")
        nuevaEdad = input("Ingrese la nueva edad (actual: " + (personaEncontrada["Edad"]) + "): ")

        personaEncontrada["Nombre"] = nuevoNombre
        personaEncontrada["Apellido"] = nuevoApellido
        personaEncontrada["Edad"] = (nuevaEdad)
        
        print("Actuliza los telefonos tambien")
        for i, tel in enumerate(personaEncontrada["Telefono"]):
            print(f"Teléfono #{i+1}")
            nuevoCodigo = input(f"Ingrese nuevo código (actual: {tel['codigo']}): ")
            nuevoNumero = input(f"Ingrese nuevo número (actual: {tel['numero']}): ")
            nuevoTipo = input(f"Ingrese nuevo tipo (actual: {tel['tipo']}): ")

            tel["codigo"] = nuevoCodigo
            tel["numero"] = nuevoNumero
            tel["tipo"] = nuevoTipo

        print("Persona Actuaizada")
    elif (opcionUsuario == 5):
     print("#################")
     print("#### Eliminar Persona ####")
     print("#################")
     idBuscado = input("Ingrese el ID de la persona que desea eliminar: ")
     personaEliminada = False

     for i, persona in enumerate(listaPersonas):
        if persona["id"] == idBuscado:
            del listaPersonas[i]
            personaEliminada = True
            print("Eliminaste una persona")
            break
        else:
         print("No se encontró una persona con ese ID.")     
    elif (opcionUsuario == 6):
      print("Gracias por usar el programa vuelve pronto")
      programa = False
      
        
        
        
# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412