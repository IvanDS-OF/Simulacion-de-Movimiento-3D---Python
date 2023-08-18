# Simulacion-de-Movimiento-3D---Python
Este programa hace una simple simulación del movimiento que se puede programar en Python usando librerías comunes

En este repositorio existen dos códigos. Ambos códigos hacen la misma simulación. 

### Code_traditional.py

Este código está escrito de forma tradicional casi por completo.

Primero importamos las librerías necesarias para la animación.

```
import numpy as np
import seaborn as sbn
impor time
import matplotlib.pyplot as plt
```

Primero colocamos las medidas de los lados del prisma y luego colocamos las coordenadas que formarán el prisma. Recordando que un prisma se compone de **aristas (unión entre vértices)** y **vértices (esquinas)** y que para formar un cubo es necesario tener 8 vértices para formar 6 caras, como se muestra en la siguiente firuga: 

![Cubo](images/home/cubo.png)



