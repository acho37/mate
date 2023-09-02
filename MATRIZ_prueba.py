matr = []
fil = int(input("nº de filas: "))
col = int(input("nº de columnas: "))
for i in range(fil):
    matr.append([0]*col)
for f in range(fil):
    for c in range(col):
        matr[f][c] = int(input("ingrese el elemento {}x{}: ".format(f,c)))
print(matr)