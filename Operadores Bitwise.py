x = 22

print ("x = {: >6b}". format ( x ) )
#X a bits (binario)
print ("x & 4 = {: >3d} = {: >6b}". format ( x & 4 , x & 4) )
#Comparar bits de x contra bits de 4 (100), revisa a la par los bits por posicion y escribe 1 si en ambos parametros existe un 1.
print ("x | 1 = {: >3d} = {: >6b}". format ( x | 1 , x | 1) )
#Comparar bits de x contra bits de 1 (1), revisa a la par los bits por posicion y escribe 1 si en almenos uno de los parametros existe un 1.
print ("x ^ 4 = {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )
#Comparar bits de x contra bits de 1 (1), revisa a la par los bits por posicion y escribe 1 si en solo uno de los parametros existe un 1.
print ("~x = {: >3d} = {: >6b}". format (~ x , ~ x ) )
#Reemplaza 1 por 0 y 0 por 1 en cada posicion.
print ("x << 1 = {: >3d} = {: >6b}". format ( x << 1 , x << 1) )
#Mueve el arreglo de bits a la izquierda y agrega 0s a la derecha, los bits excedentes a la derecha se pueden perder.
print ("x >> 2 = {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )
#Mueve el arreglo de bits a la derecha y los bits se van perdiendo segun se mueven.