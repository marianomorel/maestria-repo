import numpy as np
from scipy.interpolate import RegularGridInterpolator

# Datos de la tabla
slew_values = np.array([50, 100, 150, 200])
cload_values = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20])
delay_values = np.array([
    [52.0, 53.0, 54.0, 55, 56.0, 57.0, 58.0, 59.0, 60, 65, 75],  # Slew = 50
    [117.0, 118.0, 119.0, 120, 121.0, 122.0, 123.0, 124.0, 125, 135, 140],  # Slew = 100
    [124.0, 126.0, 128.0, 130, 132.0, 134.0, 136.0, 138.0, 140, 145, 150],  # Slew = 150
    [174.0, 176.0, 178.0, 180, 182.0, 184.0, 186.0, 188.0, 190, 200, 210]   # Slew = 200
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

print(f"Delay interpolado para slew={slew_input} ps y Cload={cload_input} fF: {delay:.2f} ps")
