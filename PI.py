#Generación de Pi utilizando un método de Montecarlo.
# Esta aproximacion por montecarlo de pi nunca va a ser exacta porque no tenemos en cuenta la frontera.

import random
from math import sqrt

cota = int(input('Valores de pi a calcular: '))  #Numero de veces que calcularemos pi para mejor estadistica
N = int(input('Número de puntos generados: '))  #Numero de dardos lanzados en cada iteracion

pi_ar = []    #Genero una lista vacia donde guardaremos los valores de pi obtenidos.

for j in range(cota): #Generamos una lista de 'cota'-elementos para recorrerla
    c = 0   #Contador de puntos dentro del circulo, inicializamos a 0.
    for i in range(N):   #generamos N puntos aleatorios
        x = random.uniform(0,1) #generamos una cordenada x aleatoria
        y = random.uniform(0,1) #generamos una cordenada y aleatoria
        d = x**2 + y**2 #calculamos la distancia del punto p=(x,y) al origen, el radio es 1.
        if d < 1:  #si entra en el circulo sumamos 1 al contador.
            c += 1
        elif d == 1.0:    #esto porque la frontera es territorio inexplorado
            print('Aquí nunca cae un número, sigue soñando.')
    Pi = 4*c/N  #calculamos el valor de pi.
    pi_ar.append(Pi)    #añadimos el valor de pi calculado a la lista de los valores obtenidos.
    c = 0    #Volvemos a poner el contador a 0, para calcular el siguiente valor.
#Aqui una vez obtenido el array con los valores de pi obtenidos, calcularemos la media de los valores.

Media = 0   #Definimos un parámetro mudo para calcular la media de los valores de pi obtenidos. 
for x in pi_ar:
    Media += x / cota

err = 0   #Definimos otro parámetro mudo para calcular la desviación.
for i in pi_ar:
    err += ((i - Media)**2) / cota
Error = sqrt(err)

print(round(Media,4))   #Redondeamos el resultado a 4 cifras significativas
print(round(Error,4))