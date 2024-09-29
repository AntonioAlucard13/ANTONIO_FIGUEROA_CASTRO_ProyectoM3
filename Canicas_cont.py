import random as rdm #Importamos la función Random, con la finalidad de generar o manipular números aleatorios, así como seleccionar elementos de listas, y le asignaremos el alias de rmd.
import matplotlib.pyplot as pplt #Importamos pyplot, que es una libreria de la biblioteca de matplotlib, con la finalidad para crear gráficos y añadir elementos a ellos, como líneas, imágenes o textos y le asignaremos el alias de pplt.

# Aquí creamos la función para simular la máquina de Galton y contar la cantidad de canicas que tendremos en cada contenedor.
def maquina_galton(numero_canicas, numero_niveles):
    # Creamos una lista llamada "contenedores", que representa la cantidad de canicas en cada contenedor, en este caso iniciamos con CERO.
    contenedores = [0] * (numero_niveles + 1)

    # Creamos el ciclo para simular el recorrido de cada una de las canicas.
    for i in range(numero_canicas):
        # Asignamos la posición de la primer canica en el primero contenedor en este caso lo asignamos en el nivel 0.
        posicion = 0
        
        # Definimos el ciclo para determinar el recorrido vertical de la canica, si cae a la derecha, baja un nivel.
        for nivel in range(numero_niveles):
            lado = rdm.choice(["Izq", "Der"])  # Definimos la asignación de escoger aleatoriamente si cae a la izquierda o a la derecha.
            if lado == "Der":
                posicion += 1  # Nuevamente asignamos que si cae a la derecha, baja un nivel.
        
        # Incrementar el contador del contenedor correspondiente a la posición final de la canica.
        contenedores[posicion] += 1
    
    return contenedores

# Aquí creamos la función para graficar el histograma que muestra la cantidad de canicas en cada contenedor.
def graf_maqgalton(datos):
    numero_contenedores = len(datos)
    x = list(range(numero_contenedores))
    pplt.bar(x, datos) #Aquí realizamos la creacion del histograma para la simulacion de la maquina de galton.
    pplt.xlabel("Número de Contenedor") #Asignamos la etiqueta del Número de contenedores.
    pplt.ylabel("Cantidad de Canicas")#Asignamos la etiqueta de la cantidad de canicas.
    pplt.title("Máquina de Galton")#Asignamos la etiqueta de la Máquina de Galton.
    pplt.xticks(x) # Numera contenedores del 0 al 12.
    pplt.grid(True)  # Mostrar una cuadrícula en el fondo del gráfico.
    pplt.show()

# Aquí configuramos la Máquina de Galton para que realice la simulación de 3000 canicas con 12 contenedores.
numero_canicas = 3000
numero_niveles = 12

# Aquí se realiza la simulación de la máquina de Galton y obtenemos los resultados.
resultados = maquina_galton(numero_canicas, numero_niveles)

# Aquí mandamos llamar la grafica del histograma con los resultados obtenidos.
graf_maqgalton(resultados)

# Creado por el Ing. Antonio Figueroa Castro
