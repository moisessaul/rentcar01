import itertools
from collections import defaultdict

# Datos históricos de números acertados (excluyendo el número complementario)
historico = [
    [4, 11, 12, 17, 27, 38],
    [2, 6, 12, 13, 30, 39],
    [13, 16, 18, 23, 29, 38],
    [10, 17, 19, 22, 36, 39],
    [2, 10, 13, 15, 24, 36],
    [2, 21, 24, 28, 35, 40],
    [1, 2, 16, 20, 26, 35],
    [13, 15, 25, 28, 35, 39],
    [1, 2, 5, 21, 28, 38],
    [18, 19, 23, 26, 28, 40],
    [2, 13, 16, 17, 18, 19],
    [9, 15, 17, 20, 24, 29]
]

# Crear un diccionario para contar la frecuencia de cada número
frecuencia_numeros = defaultdict(int)

for combinacion in historico:
    for numero in combinacion:
        frecuencia_numeros[numero] += 1

# Ordenar los números por frecuencia (de mayor a menor)
numeros_ordenados = sorted(frecuencia_numeros.keys(), key=lambda x: frecuencia_numeros[x], reverse=True)

print("Números ordenados por frecuencia de aciertos:")
for num in numeros_ordenados:
    print(f"Número {num}: {frecuencia_numeros[num]} veces")

# Función para calcular la probabilidad de acierto de una combinación
def calcular_probabilidad(combinacion):
    aciertos = 0
    total_combinaciones = len(historico)
    
    for comb_historica in historico:
        comunes = len(set(combinacion) & set(comb_historica))
        if comunes >= 3:  # Consideramos acierto si hay 3 o más números en común
            aciertos += 1
    
    probabilidad = aciertos / total_combinaciones
    return probabilidad

# Generar todas las combinaciones posibles de 6 números con los más frecuentes
numeros_mas_frecuentes = numeros_ordenados[:12]  # Tomamos los 12 números más frecuentes
combinaciones = itertools.combinations(numeros_mas_frecuentes, 6)

# Evaluar las combinaciones y guardar las mejores
mejores_combinaciones = []
for comb in combinaciones:
    prob = calcular_probabilidad(comb)
    mejores_combinaciones.append((comb, prob))

# Ordenar las combinaciones por probabilidad (de mayor a menor)
mejores_combinaciones.sort(key=lambda x: x[1], reverse=True)

# Mostrar las 10 mejores combinaciones
print("\nTop 10 combinaciones con mayor probabilidad de acierto:")
for i, (comb, prob) in enumerate(mejores_combinaciones[:10], 1):
    print(f"{i}. Combinación: {sorted(comb)} - Probabilidad: {prob:.2%}")