import random


def list_of_consecutives(list_to_check: list) -> bool:
    """Devuelve True si todos los números de la lista son consecutivos,
    estos pueden ser ascendentes o descendentes, ordenados o no

    Args:
        list_to_check (list): Lista de valores enteros

    Returns:
        bool: True sin son consecutivos
    """
    return sorted(list_to_check) == list(range(min(list_to_check), max(list_to_check)+1))


def get_matriz_of_random_values(x: int, y: int, max_num: int) -> list:
    """Devuelve una matriz de valores random, de dimensiones x * y
    Siendo max_num el valor mayor random esperado

    Args:
        x (int): largo
        y (int): alto
        max_num (int): Mayor valor a devolver

    Returns:
        list: Matriz x * y de valores aleatorios
    """

    matriz = []

    for i in range(x):
        matriz.append([])
        for j in range(y):
            matriz[i].append(random.randint(1, max_num))

    return matriz


def generate_matriz_random() -> tuple:
    """ Crea una matriz de 5x5 randomizada (1 a 10) con números enteros.
    Si encuentra secuencia de 4 números consecutivos horizontal o vertical,
    se muestra la posición inicial y final.
    Retorna una tupla, donde el primer elelemento es la matriz y el segundo la
    lista de resultados exitosos
    """
    matriz = get_matriz_of_random_values(5, 5, 5)
    successful_results = []

    for i in range(0, 1):
        for j in range(0, 1):
            # Pruebo horizontalmente 4 valores
            values_to_check = matriz[j][i:i+4]
            if list_of_consecutives(values_to_check):
                successful_results.append(values_to_check)

            # Pruebo verticalmente 4 valores
            values_to_check = [matriz[j][i], matriz[j+1][i], matriz[j+2][i], matriz[j+3][i]]
            if list_of_consecutives(values_to_check):
                successful_results.append(values_to_check)

    return matriz, successful_results
