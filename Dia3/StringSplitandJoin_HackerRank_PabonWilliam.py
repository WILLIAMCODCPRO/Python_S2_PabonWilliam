# ####################
# # #### Dia 3  ######
# #####################

def split_and_join(line):
    palabras = line.split(" ")
    result = "-".join(palabras)
    return result


line = input()
result = split_and_join(line)
print(result)

# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412