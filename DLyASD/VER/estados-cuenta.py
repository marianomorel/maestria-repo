import networkx as nx
import matplotlib.pyplot as plt

def transicion(estado, caracter):
    if estado == 0 and caracter == 'c':
        return 1
    elif estado == 1 and caracter == 'a':
        return 2
    elif estado == 2 and caracter == 's':
        return 3
    elif estado == 3 and caracter != 'a':
        return 0
    elif estado == 3 and caracter == 'a':
        return 4
    elif estado == 4 and caracter == ' ':
        return 5
    elif estado == 5 and caracter == ' ':
        return 6
    else:
        return 0

def contar_ocurrencias(frase):
    estado_actual = 0
    ocurrencias_casa = 0
    for caracter in frase:
        if estado_actual == 0 and caracter == 'c':
            estado_actual = 1
        elif estado_actual == 1 and caracter == 'a':
            estado_actual = 2
        elif estado_actual == 2 and caracter == 's':
            estado_actual = 3
        elif estado_actual == 3 and caracter == 'a':
            estado_actual = 4
        elif estado_actual == 4 and caracter == ' ':
            estado_actual = 5
            ocurrencias_casa += 1
            estado_actual = 0  # Reiniciar para buscar más ocurrencias
        else:
            estado_actual = 0  # Reiniciar si la secuencia no es válida
    return ocurrencias_casa

# Crear el grafo
G = nx.DiGraph()

# Agregar nodos
for i in range(7):
    G.add_node(i, label=str(i))

# Agregar bordes
for i in range(6):
    G.add_edge(i, i+1)

# Obtener posiciones de los nodos
pos = nx.spring_layout(G)

# Dibujar nodos y etiquetas de los nodos
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='skyblue')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Dibujar bordes
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, arrows=True)

# Mostrar el diagrama
plt.axis('off')
plt.show()

# Contar ocurrencias en la frase dada
frase = "estoy en casa pero si no queres venir paso por tu casa y nos casamos en la casa del casamiento"
ocurrencias = contar_ocurrencias(frase)
print("Número de ocurrencias de 'casa ':", ocurrencias)
