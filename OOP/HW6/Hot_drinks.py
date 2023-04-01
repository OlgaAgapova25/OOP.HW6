from Product import Product


class Hot_drinks(Product):

    def __init__(self, name, volume, temp):
        super().__init__(name, volume)
        self._temp = temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, new_temp):
        self._temp = new_temp

    def __str__(self) -> str:
        return f'{self._name} {str(self._volume)} {str(self._temp)}'