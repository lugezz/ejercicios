import unittest

from clases.utils import Circulo, WrongMultiplyException, WrongRadiusException


class TestClases(unittest.TestCase):
    def setUp(self):
        self.circle = Circulo()

    def test_calc_ok(self):
        """testea los cálculos con resultados ok
        """
        self.circle.radio = 5
        perimetro = round(self.circle.get_perimetro(), 2)
        area = round(self.circle.get_area(), 2)

        self.assertEqual(perimetro, 31.42)
        self.assertEqual(area, 78.54)

    def test_empty_radius(self):
        """testea los cálculos sin el dato de radio (default = 1)
        """
        perimetro = round(self.circle.get_perimetro(), 2)
        area = round(self.circle.get_area(), 2)

        self.assertEqual(perimetro, 6.28)
        self.assertEqual(area, 3.14)

    def test_wrong_info(self):
        """testea los errores por datos incorrectos en radio
        """

        with self.assertRaises(WrongRadiusException):
            self.circle.radio = -2

        with self.assertRaises(WrongRadiusException):
            self.circle.radio = 'a'

    def test_calc_ok_mult(self):
        """testea los cálculos con resultados ok
        """
        self.circle.radio = 5
        new_circle = self.circle * 3
        perimetro = round(new_circle.get_perimetro(), 2)
        area = round(new_circle.get_area(), 2)

        self.assertEqual(perimetro, 94.25)
        self.assertEqual(area, 706.86)

    def test_empty_radius_mult(self):
        """testea los cálculos sin el dato de radio (default = 1)
        """
        new_circle = self.circle * 3
        perimetro = round(new_circle.get_perimetro(), 2)
        area = round(new_circle.get_area(), 2)

        self.assertEqual(perimetro, 18.85)
        self.assertEqual(area, 28.27)

    def test_wrong_info_mult(self):
        """testea los errores por datos incorrectos en radio
        """

        with self.assertRaises(WrongMultiplyException):
            self.circle * -3

        with self.assertRaises(WrongMultiplyException):
            self.circle * 'a'


if __name__ == '__main__':
    unittest.main()
