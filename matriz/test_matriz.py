import unittest

from matriz.utils import generate_matriz_random


class TestSimple(unittest.TestCase):
    def test_generated_list(self):
        """testea la longitud de la matriz
        """
        first_matriz = generate_matriz_random()[0]

        self.assertEqual(len(first_matriz), 5)
        self.assertEqual(len(first_matriz[-1]), 5)

    def test_successful_results(self):
        """testea los resultados exitosos de las listas consecutivas
        """
        consecutive_lists = []
        while consecutive_lists == []:
            consecutive_lists = generate_matriz_random()[-1]

        sorted_consecutive_list = sorted(consecutive_lists[0])
        expected_result = [x for x in range(sorted_consecutive_list[0], sorted_consecutive_list[0] + 4)]

        self.assertEqual(len(consecutive_lists[0]), 4)
        self.assertEqual(expected_result, sorted_consecutive_list)


if __name__ == '__main__':
    unittest.main()
