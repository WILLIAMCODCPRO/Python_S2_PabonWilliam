# ####################
# # #### Dia 3  ######
# #####################

N = int(input())
    
lista = [] 

for _ in range(N):
        entrada = input().split()
        comando = entrada[0]

        if comando == 'insert':
            posicion = int(entrada[1])
            elemento = int(entrada[2])
            lista.insert(posicion, elemento)
        elif comando == 'print':
            print(lista)
        elif comando == 'remove':
            elemento = int(entrada[1])
            lista.remove(elemento)
        elif comando == 'append':
            elemento = int(entrada[1])
            lista.append(elemento)
        elif comando == 'sort':
            lista.sort()
        elif comando == 'pop':
            lista.pop()
        elif comando == 'reverse':
            lista.reverse()

# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412