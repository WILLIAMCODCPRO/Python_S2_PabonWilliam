# ####################
# # #### Dia 3 ######
# #####################

puntajeEstuiantes=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        puntajeEstuiantes.append([name,score])
grades = sorted(set([score for name, score in puntajeEstuiantes]))
segundaNotaMasBaja = grades[1]

segundaNotaMasBajaEstudiantes = [name for name, score in puntajeEstuiantes if score == segundaNotaMasBaja]

for name in sorted(segundaNotaMasBajaEstudiantes):
    print(name)

# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412