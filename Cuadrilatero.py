up = eval(input("Ingrese medida del lado superior (\"Solo numero\"): "))
down = eval(input("Ingrese medida del lado inferior (\"Solo numero\"): "))
left = eval(input("Ingrese medida del lado izquierdo (\"Solo numero\"): "))
right = eval(input("Ingrese medida del lado derecho (\"Solo numero\"): "))

if (up == down) and (down == left) and (left == right): print("Cuadrado")
elif (up == down) and (left == right) and (up != left): print("Rectangulo")
else: print("Otro cuadrilatero")