# Código para hacer la animación de los 4 movimientos necesarioas para
# el análisis de nuestro problema :

# Importamos librerías
# Import all the needed libraries

import numpy as np
import seaborn as sbn
import time 
import matplotlib.pyplot as plt

# Load an Seaborn style

sbn.set_style ("white")

# Lados del cubo
# Cube sides size

ax = 3
ay = 0.5
az = 3

# Generamos puntos y uniones para hacer el cubo
# Build the entire cube
#      a,   b,  c,   d,   a,   e,  f,  g,  h,   e,   h,   d,   h,   g,  c,  b,  f
x1 = [-ax, ax, ax, -ax, -ax, -ax, ax, ax, -ax, -ax, -ax, -ax, -ax, ax, ax, ax, ax]
y1 = [-ay, -ay, ay, ay, -ay, -ay, -ay, ay, ay, -ay, ay, ay, ay, ay, ay, -ay, -ay]
z1 = [-az, -az, -az, -az, -az, az, az, az, az, az, az, -az, az, az, -az, -az, az]
Tras = [1, 1, 1, 1, 1, 1, 1 ,1, 1, 1 ,1, 1 ,1 ,1, 1 ,1 ,1] #Matriz UNO importante
# This matrix helps us to construct the transformation full matrices later. 

# Main matrix - It can be manipulated to move the cube.
m_prin = [x1, y1, z1, Tras] # Matriz principal

x=np.arange(0,2*np.pi,0.1) # X
FUNX=np.sin(x)*2 # Define the movement function

# Inicializamos figura en 3D
# Initialize the 3d figure
plt.figure(figsize = (12, 10))
plot_axes = plt.axes(projection = '3d') # Use "plt" commands
plot_axes.set_title("3D simulation movement")

# Pause among frames simulation
pauseV = 0.001 # Seconds

# ***************************
# Comenzamos con la animación. 
# Start the simulation


# Movimiento TRASLACIONAL en X
# Traslational movement -> X

for i in range(len(FUNX)):
	k1 = FUNX[i]
	P1 = [[1, 0, 0, k1], # IMPORTANTE: COLOCAR LA FUNCIÓN EN X -> ULTIMA POSICIÓN
		  [0, 1, 0, 0], 
		  [0, 0, 1, 0], 
		  [0, 0, 0, 1]]
	SA = np.dot(P1, m_prin)
	plot_axes.plot(SA[0], SA[1], SA[2], c="b")
	plot_axes.plot(x1, y1, z1, c="0.6")
	plot_axes.scatter(0, 0, 0, c="r", lw=4) #Marcamos el centro
	plot_axes.scatter([-5, 5], [-5, 5], [-5, 5], c="w") #Fijamos límites
	plot_axes.scatter(SA[0][0], SA[1][0], SA[2][0], c="m", lw=4)
	plot_axes.scatter(SA[0][1], SA[1][1], SA[2][1], c="m", lw=4)
	plot_axes.scatter(SA[0][5], SA[1][5], SA[2][5], c="m", lw=4)
	plot_axes.scatter(SA[0][6], SA[1][6], SA[2][6], c="m", lw=4)
	'''	
	plot_axes.text(SA[0][0], SA[1][0], SA[2][0], 
		          (str(SA[0][0]), str(SA[1][0]), str(SA[2][0])))
	plot_axes.text(SA[0][1], SA[1][1], SA[2][1], 
		          (str(SA[0][1]), str(SA[1][1]), str(SA[2][1])))
	plot_axes.text(SA[0][5], SA[1][5], SA[2][5], 
		          (str(SA[0][5]), str(SA[1][5]), str(SA[2][5])))
	plot_axes.text(SA[0][6], SA[1][6], SA[2][6], 
		          (str(SA[0][6]), str(SA[1][6]), str(SA[2][6])))
	'''
	plot_axes.set_xlabel('x')
	plot_axes.set_ylabel('y')
	plot_axes.set_zlabel('z')
	plot_axes.set_title("3D simulation movement")
	plt.pause(pauseV)
	plt.cla()

for i in range(len(FUNX)):
	k1 = FUNX[i]
	P1 = [[1, 0, 0, 0], #IMPORTANTE: COLOCAR LA FUNCIÓN EN X -> ULTIMA POSICIÓN
		  [0, 1, 0, k1], 
		  [0, 0, 1, 0], 
		  [0, 0, 0, 1]]
	SA = np.dot(P1, m_prin)
	plot_axes.plot(SA[0], SA[1], SA[2], c="b")
	plot_axes.plot(x1, y1, z1, c="0.6")
	plot_axes.scatter(0, 0, 0, c="r", lw=4) #Marcamos el centro
	plot_axes.scatter([-5, 5], [-5, 5], [-5, 5], c="w") #Fijamos límites
	plot_axes.scatter(SA[0][0], SA[1][0], SA[2][0], c="m", lw=4)
	plot_axes.scatter(SA[0][1], SA[1][1], SA[2][1], c="m", lw=4)
	plot_axes.scatter(SA[0][5], SA[1][5], SA[2][5], c="m", lw=4)
	plot_axes.scatter(SA[0][6], SA[1][6], SA[2][6], c="m", lw=4)
	'''
	plot_axes.text(SA[0][0], SA[1][0], SA[2][0], 
		          (str(SA[0][0]), str(SA[1][0]), str(SA[2][0])))
	plot_axes.text(SA[0][1], SA[1][1], SA[2][1], 
		          (str(SA[0][1]), str(SA[1][1]), str(SA[2][1])))
	plot_axes.text(SA[0][5], SA[1][5], SA[2][5], 
		          (str(SA[0][5]), str(SA[1][5]), str(SA[2][5])))
	plot_axes.text(SA[0][6], SA[1][6], SA[2][6], 
		          (str(SA[0][6]), str(SA[1][6]), str(SA[2][6])))
    	'''
	plot_axes.set_xlabel('x')
	plot_axes.set_ylabel('y')
	plot_axes.set_zlabel('z')
	plot_axes.set_title("3D simulation movement")
	plt.pause(pauseV)
	plt.cla()


for i in range(len(FUNX)):
	k1 = FUNX[i]     
	P1 = [[np.cos(k1), 0, -np.sin(k1), 0], #Rotación eje Z
	      [0, 1, 0, 0],
	      [np.sin(k1), 0, np.cos(k1), 0], 
	      [0, 0, 0, 1]]      
	SA = np.dot(P1, m_prin)
	plot_axes.plot(SA[0], SA[1], SA[2], c="b")
	plot_axes.plot(x1, y1, z1, c="0.6")
	plot_axes.scatter(0, 0, 0, c="r", lw=4)
	plot_axes.scatter([-5, 5], [-5, 5], [-5, 5], c="w")
	plot_axes.scatter(SA[0][0], SA[1][0], SA[2][0], c="m", lw=4)
	plot_axes.scatter(SA[0][1], SA[1][1], SA[2][1], c="m", lw=4)
	plot_axes.scatter(SA[0][5], SA[1][5], SA[2][5], c="m", lw=4)
	plot_axes.scatter(SA[0][6], SA[1][6], SA[2][6], c="m", lw=4)
	'''
	plot_axes.text(SA[0][0], SA[1][0], SA[2][0], 
		          (str(SA[0][0]), str(SA[1][0]), str(SA[2][0])))
	plot_axes.text(SA[0][1], SA[1][1], SA[2][1], 
		          (str(SA[0][1]), str(SA[1][1]), str(SA[2][1])))
	plot_axes.text(SA[0][5], SA[1][5], SA[2][5], 
		          (str(SA[0][5]), str(SA[1][5]), str(SA[2][5])))
	plot_axes.text(SA[0][6], SA[1][6], SA[2][6], 
		          (str(SA[0][6]), str(SA[1][6]), str(SA[2][6])))
	'''
	plot_axes.set_xlabel('x')
	plot_axes.set_ylabel('y')
	plot_axes.set_zlabel('z')
	plot_axes.set_title("3D simulation movement")
	plt.pause(pauseV)
	plt.cla()

for i in range(len(FUNX)):
	
	k1 = FUNX[i]
	P1 = [[1, 0, 0, 0], #Rotación eje Z
	      [0, np.cos(k1), np.sin(k1), 0], #Rotación sobre eje Y
	      [0, -np.sin(k1), np.cos(k1), 0], 
	      [0, 0, 0, 1]]     
	SA = np.dot(P1, m_prin)
	plot_axes.plot(SA[0], SA[1], SA[2], c="b")
	plot_axes.plot(x1, y1, z1, c="0.6")
	plot_axes.scatter(0, 0, 0, c="r", lw=4)
	plot_axes.scatter([-5, 5], [-5, 5], [-5, 5], c="w")
	plot_axes.scatter(SA[0][0], SA[1][0], SA[2][0], c="m", lw=4)
	plot_axes.scatter(SA[0][1], SA[1][1], SA[2][1], c="m", lw=4)
	plot_axes.scatter(SA[0][5], SA[1][5], SA[2][5], c="m", lw=4)
	plot_axes.scatter(SA[0][6], SA[1][6], SA[2][6], c="m", lw=4)
	'''
	plot_axes.text(SA[0][0], SA[1][0], SA[2][0], 
		          (str(SA[0][0]), str(SA[1][0]), str(SA[2][0])))
	plot_axes.text(SA[0][1], SA[1][1], SA[2][1], 
		          (str(SA[0][1]), str(SA[1][1]), str(SA[2][1])))
	plot_axes.text(SA[0][5], SA[1][5], SA[2][5], 
		          (str(SA[0][5]), str(SA[1][5]), str(SA[2][5])))
	plot_axes.text(SA[0][6], SA[1][6], SA[2][6], 
		          (str(SA[0][6]), str(SA[1][6]), str(SA[2][6])))
	'''
	plot_axes.set_xlabel('x')
	plot_axes.set_ylabel('y')
	plot_axes.set_zlabel('z')
	plot_axes.set_title("3D simulation movement")
	plt.pause(pauseV)
	plt.cla()



for i in range(len(FUNX)):
	k1 = FUNX[i]
	P1 = [[1, 0, 0, k1], #Rotación eje Z
	      [0, 1, 0, k1], #Rotación sobre eje Y
	      [0, 0, 1, 0], 
	      [0, 0, 0, 1]]
	'''P1 = [[np.cos(k1), 0, -np.sin(k1), k1], #Rotación eje Z
	      [0, np.cos(k1), np.sin(k1), k1], #Rotación sobre eje Y
	      [np.sin(k1), -np.sin(k1), np.cos(k1), 0], 
	      [0, 0, 0, 1]]  '''   
	SA = np.dot(P1, m_prin)
	plot_axes.plot(SA[0], SA[1], SA[2], c="b")
	plot_axes.plot(x1, y1, z1, c="0.6")
	plot_axes.scatter(0, 0, 0, c="r", lw=4)
	plot_axes.scatter([-5, 5], [-5, 5], [-5, 5], c="w")
	plot_axes.scatter(SA[0][0], SA[1][0], SA[2][0], c="m", lw=4)
	plot_axes.scatter(SA[0][1], SA[1][1], SA[2][1], c="m", lw=4)
	plot_axes.scatter(SA[0][5], SA[1][5], SA[2][5], c="m", lw=4)
	plot_axes.scatter(SA[0][6], SA[1][6], SA[2][6], c="m", lw=4)
	'''	
	plot_axes.text(SA[0][0], SA[1][0], SA[2][0], 
		          (str(SA[0][0]), str(SA[1][0]), str(SA[2][0])))
	plot_axes.text(SA[0][1], SA[1][1], SA[2][1], 
		          (str(SA[0][1]), str(SA[1][1]), str(SA[2][1])))
	plot_axes.text(SA[0][5], SA[1][5], SA[2][5], 
		          (str(SA[0][5]), str(SA[1][5]), str(SA[2][5])))
	plot_axes.text(SA[0][6], SA[1][6], SA[2][6], 
		          (str(SA[0][6]), str(SA[1][6]), str(SA[2][6])))
	'''
	plot_axes.set_xlabel('x')
	plot_axes.set_ylabel('y')
	plot_axes.set_zlabel('z')
	plot_axes.set_title("3D simulation movement")
	plt.pause(pauseV)
	plt.cla()


for i in range(len(FUNX)):
	k1 = FUNX[i]
	P1R = [[np.cos(k1), 0, -np.sin(k1), 0], #Rotación eje Z
	      [0, 1, 0, 0],
	      [np.sin(k1), 0, np.cos(k1), 0], 
	      [0, 0, 0, 1]] 
	P2R = [[1, 0, 0, 0], #Rotación eje Z
	      [0, np.cos(k1), np.sin(k1), 0], #Rotación sobre eje Y
	      [0, -np.sin(k1), np.cos(k1), 0], 
	      [0, 0, 0, 1]]
	SA = np.dot(np.dot(P2R, P1R), m_prin)
	plot_axes.plot(SA[0], SA[1], SA[2], c="b")
	plot_axes.plot(x1, y1, z1, c="0.6")
	plot_axes.scatter(0, 0, 0, c="r", lw=4)
	plot_axes.scatter([-5, 5], [-5, 5], [-5, 5], c="w")
	plot_axes.scatter(SA[0][0], SA[1][0], SA[2][0], c="m", lw=4)
	plot_axes.scatter(SA[0][1], SA[1][1], SA[2][1], c="m", lw=4)
	plot_axes.scatter(SA[0][5], SA[1][5], SA[2][5], c="m", lw=4)
	plot_axes.scatter(SA[0][6], SA[1][6], SA[2][6], c="m", lw=4)
	'''
	plot_axes.text(SA[0][0], SA[1][0], SA[2][0], 
		          (str(SA[0][0]), str(SA[1][0]), str(SA[2][0])))
	plot_axes.text(SA[0][1], SA[1][1], SA[2][1], 
		          (str(SA[0][1]), str(SA[1][1]), str(SA[2][1])))
	plot_axes.text(SA[0][5], SA[1][5], SA[2][5], 
		          (str(SA[0][5]), str(SA[1][5]), str(SA[2][5])))
	plot_axes.text(SA[0][6], SA[1][6], SA[2][6], 
		          (str(SA[0][6]), str(SA[1][6]), str(SA[2][6])))
	'''
	plot_axes.set_xlabel('x')
	plot_axes.set_ylabel('y')
	plot_axes.set_zlabel('z')
	plot_axes.set_title("3D simulation movement")
	plt.pause(pauseV)
	plt.cla()


