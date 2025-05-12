 ####################
# # #### Dia 3 ######
# #####################

n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()

marks = student_marks[query_name]
total = 0
contador = 0
for nota in marks:
    total += nota
    contador += 1

promedio = total / contador
print("{:.2f}".format(promedio))

# Desarrollado por : William Santiago Pabon Ardila - C.C:1.006.798.412