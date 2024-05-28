import matplotlib.pyplot as plt
import numpy as np

# Definir las coordenadas de los puntos en el círculo
num_estados = 7
theta = np.linspace(0, 2*np.pi, num_estados, endpoint=False)
radius = 2  # Aumentar el radio para espaciar más los estados

x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Modificar la posición de Q6 ligeramente
x[5] *= 1.1
y[5] *= 1.1

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Dibujar los círculos para los estados
circle_radius = 0.3
for i in range(num_estados):
    circle = plt.Circle((x[i], y[i]), radius=circle_radius, color='lightgrey', ec='black')
    ax.add_artist(circle)

# Dibujar el círculo para el estado central
center_circle = plt.Circle((0, 0), radius=circle_radius, color='lightgrey', ec='black')
ax.add_artist(center_circle)

# Anotar los estados
estados = ['Q{}'.format(i) for i in range(num_estados)]
for i, txt in enumerate(estados):
    ax.annotate(txt, (x[i], y[i]), fontsize=12, ha='center', va='center', color='black')

# Anotar el estado central
ax.annotate('Q7', (0, 0), fontsize=12, ha='center', va='center', color='black')

# Configuración de los ejes
ax.set_aspect('equal')  # Igualar la escala de los ejes
ax.set_xlim(-2.5, 2.5)  # Ajustar los límites de los ejes x para visualizar completamente los estados
ax.set_ylim(-2.5, 2.5)  # Ajustar los límites de los ejes y para visualizar completamente los estados
ax.axis('off')  # Ocultar ejes

# Mostrar el gráfico
plt.show()
