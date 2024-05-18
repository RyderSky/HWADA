val1 = eval(input("Ingrese un numero mayor a 0: "))
val2 = eval(input("Ingrese un numero mayor a 0: "))
min = 0
mcm = 1
if(val1 <= 0 or val2 <= 0):
    print("Error, un numero es menor o igual a 0: ")
    exit()
if(val1 > val2):
    min = val2
else:
    min = val1
for x in range(1, min+1):
    if((val1 % x) == 0 and (val2 % x) == 0):
        mcm = x
print(mcm)
if(mcm == 1):
    print("Los numeros ", val1, " y ", val2, " son coprimos")
