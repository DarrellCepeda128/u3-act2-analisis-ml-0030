
# Cepeda Darrell NC = 0030   Fecha 6/11/2026
# importar librerias
import pandas as pd
import numpy as np
print("Diagnóstico de Salud  Cepeda Darrell NC = 0030")

pacientes = {
    "Nombre": ["Ana", "Luis", "Marta", "Roberto", "Carla", "Javier"],
    "Presion_Arterial": [120, 140, 135, 120, 150, 125],
    "Fumador": [False, True, False, False, True, True],
    "Nivel_Riesgo": ["Bajo", "Alto", "Medio", "Bajo", "Alto", "Medio"]
}

df = pd.DataFrame(pacientes)
print(df)
print(" .*.*.*.*.*.*.* Agrupar por una sola columna Presion Arterial      NC 0030 *.*.*.*.*.*.*.*.")
agrupado = df.groupby('Presion_Arterial')
print(agrupado)
print(" .*.*.*.*.*.* Agrupar por una sola columna  0030 *.*.*.*.*.*.*.")
# calificacion promedio por departamento
print(agrupado['Presion_Arterial'].mean())

# Presion_Arterial maxima
print(agrupado['Nivel_Riesgo'].max())