import math


class WrongRadiusException(Exception):
    """Error de validación de radio con valores
    """
    pass


class WrongMultiplyException(Exception):
    """Error de validación del multiplicador
    """
    pass


class Circulo:
    # Valor inicial del radio
    _radio = 1

    @property
    def radio(self):
        """ Obtiene el radio"""
        return self._radio

    @radio.setter
    def radio(self, value: int):
        """ Define el radio"""
        if type(value) != int:
            raise WrongRadiusException('Defina un valor numérico')

        if value <= 0:
            raise WrongRadiusException('Defina un valor positivo para el radio')

        self._radio = value

    def get_area(self):
        return math.pi * self._radio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self._radio

    def __mul__(self, multiplicador):
        if type(multiplicador) != int:
            raise WrongMultiplyException('Defina un valor numérico')

        if multiplicador <= 0:
            raise WrongMultiplyException('Defina un valor positivo para el radio')

        new_el = Circulo()
        new_el.radio = multiplicador * self._radio

        return new_el
