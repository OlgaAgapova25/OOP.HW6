from Vending_machine import Vending_machine

class Hot_drinks_machine(Vending_machine):
    def __init__(self):
        my_list = []
        self._list = my_list

    def init_product(self, product):
        self._list.append(product)

    def get_product(self, product):
        for el in self._list:
            if (el == product):
                print(str(el))
    # def __init__(self, name, volume, temp):
    #     super().__init__(name)
    #     super().__init__(volume)
    #     self._temp = temp
    #
    # @property
    # def temp(self):
    #     return self._temp
    #
    # @temp.setter
    # def temp(self, new_temp):
    #     self._temp = new_temp
    #
    # def __str__(self) -> str:
    #     return f'{self._name} {str(self._volume)} {str(self._temp)}'