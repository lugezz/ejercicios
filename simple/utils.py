import random


def generate_list_of_dicts() -> list:
    """ Genera una lista de 10 diccionarios que contienen
    - Id
    - Edad: Aleatorio entre 1 y 100

    Returns:
        list: Lista de 10 elementos con id y edad
    """
    resp = []

    for i in range(1, 11):
        this_dict = {
            'id': i,
            'edad': random.randint(1, 100)
        }
        resp.append(this_dict)

    return resp


def sort_list_of_dict(list_to_sort: list) -> list:
    """Ordena la lista de diccionarios por edad de mayor a menor

    Args:
        list_to_sort (list): Lista de diccionarios con id y edad.

    Returns:
        list: Devuelve la lista ordenada por edad
    """

    sorted_list = sorted(list_to_sort, key=lambda d: d['edad'], reverse=True)

    print(f"El id de la persona más vieja ({sorted_list[0]['edad']} años) es {sorted_list[0]['id']}")
    print(f"El id de la persona más joven ({sorted_list[-1]['edad']} años) es {sorted_list[-1]['id']}")

    return sorted_list
