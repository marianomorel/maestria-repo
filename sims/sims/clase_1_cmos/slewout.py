import numpy as np
from scipy.interpolate import RegularGridInterpolator

# Datos de la tabla
slew_values = np.array([50, 100, 150, 200])
cload_values = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20])
delay_values = np.array([
    [58, 59, 60, 60, 61, 62, 63, 64, 65, 70, 90],  # Slew = 50
    [108, 109, 110, 110, 111, 112, 113, 114, 115, 120, 135],  # Slew = 100
    [118, 119, 120, 120, 121, 122, 123, 124, 125, 130, 150],  # Slew = 150
    [158, 159, 160, 160, 161, 162, 163, 164, 165, 170, 190]   # Slew = 200
])

# Crear un interpolador
interpolator = RegularGridInterpolator((slew_values, cload_values), delay_values)

# Función para obtener el delay a partir de un slew y Cload dados
def get_delay(slew, cload):
    point = np.array([[slew, cload]])  # Crear un punto para la interpolación
    return interpolator(point)[0]

# Ejemplo de uso
slew_input = 114.92  # Por ejemplo, 120 ps
cload_input = 2  # Por ejemplo, 5 fF
delay = get_delay(slew_input, cload_input)

print(f"slew_out interpolado para slew={slew_input} ps y Cload={cload_input} fF: {delay:.2f} ps")