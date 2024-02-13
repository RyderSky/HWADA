side = []

for x in range(4):
    pos = x+1
    side.append(eval(input("Ingrese valor para posicion {0}: ".format(pos))))
     
side.sort()
if side[0] == side[3]: print("Cuadrado")
elif side[0] == side[1] and side[2] == side[3]: print("Rectangulo")
else: print("Otro tipo de cuadrilatero")